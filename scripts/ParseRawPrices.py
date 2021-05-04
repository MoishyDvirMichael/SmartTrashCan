import json
import xmltodict
import re
from collections import OrderedDict
from xml.etree import ElementTree as et
from firebase_admin import credentials, firestore
import firebase_admin
import requests
from lxml import html


def deleteIrelevantRows(src_path, dst_path):
    regex = '( ){6}(<)(PriceUpdateDate|ItemType|ManufacturerName|ManufactureCountry|ManufacturerItemDescription|UnitQty|Quantity|bIsWeighted|UnitOfMeasure|QtyInPackage|ItemPrice|UnitOfMeasurePrice|AllowDiscount|ItemStatus|ItemId)([^\n]*)\n'
    with open(src_path, encoding='utf8') as src_file:
        src_text = src_file.read()
        src_file.close()
        trimmed_text = re.sub(regex,'',src_text)
        with open(dst_path, 'w', encoding='utf8') as dst_file:
            dst_file.write(trimmed_text)
            dst_file.close()
    pass

def merge2Prices(rami_levy, shupersal, both):
    with open(rami_levy, 'r', encoding='utf8') as rami_levy_file:
        rami_levy_text = rami_levy_file.read()
        rami_levy_file.close()
        with open(shupersal, 'r', encoding='utf8') as shupersal_file:
            shupersal_text = shupersal_file.read()
            shupersal_file.close()
            
            rami_levy_dict = xmltodict.parse(rami_levy_text)
            shupersal_dict = xmltodict.parse(shupersal_text)

            rami_levy_dict = OrderedDict([('root', v) if k.lower() == 'root' else (k, v) for k, v in rami_levy_dict.items()])
            shupersal_dict = OrderedDict([('root', v) if k.lower() == 'root' else (k, v) for k, v in shupersal_dict.items()])

            both_dict = {'root':OrderedDict([('RamiLevy',rami_levy_dict.get('root')),('Shupersal',shupersal_dict.get('root'))])}
            both_xml = xmltodict.unparse(both_dict)
            with open(both, 'w', encoding='utf8') as both_file:
                both_file.write(both_xml)
                both_file.close()

def xml2jsonFile(xml_path, json_path):
    with open(xml_path, encoding='utf8') as xml_file:
        xml_text = xml_file.read()
        data_dict = xmltodict.parse(xml_text)
        xml_file.close()
        json_data = json.dumps(data_dict, ensure_ascii=False)
        with open(json_path, 'w', encoding='utf8') as json_file:
            json_file.write(json_data)
            json_file.close()

def deleteDuplicationItems(duplication_path, no_duplication_path):
    with open(duplication_path, encoding='utf8') as json_file:
        data_dict = json.load(json_file)
        json_file.close()

        rami_levy_items = data_dict['root']['RamiLevy']['Items']['Item']
        shupersal_items = data_dict['root']['Shupersal']['Items']['Item']
        rami_levy_size = len(rami_levy_items)
        shupersal_size = len(shupersal_items)
        rami_levy_items_dic = {item['ItemCode']:item for item in rami_levy_items}
        shupersal_items_dic = {item['ItemCode']:item for item in shupersal_items}
        for key, item in rami_levy_items_dic.items():
            item['Source'] = 'Rami Levy'
        for key, item in shupersal_items_dic.items():
            item['Source'] = 'Shupersal'
        all_items_w_duplicate = [*shupersal_items_dic.keys(), *rami_levy_items_dic.keys()]

        duplication = [key for key in shupersal_items_dic.keys() if key in rami_levy_items_dic.keys()]
        not_duplicated = [key for key in all_items_w_duplicate if key not in duplication]

        same_name_keys = [key for key in duplication if rami_levy_items_dic[key]['ItemName'] == shupersal_items_dic[key]['ItemName']]
        
        # lines = [f"{key}:\n{rami_levy_items_dic[key]['ItemName']}\n{shupersal_items_dic[key]['ItemName']}\n\n" for key in duplication]
        # with open('../data/products/DuplicatedNames.txt', 'w', encoding='utf8') as file:
        #     file.writelines(lines)
        #     file.close()

        longer_name = {key: (rami_levy_items_dic[key] if len(rami_levy_items_dic[key]['ItemName']) > len(shupersal_items_dic[key]['ItemName']) else shupersal_items_dic[key]) for key in duplication}
        all_items = {**{key:(shupersal_items_dic[key] if key in shupersal_items_dic else rami_levy_items_dic[key]) for key in not_duplicated},**longer_name}
        
        with open(no_duplication_path, 'w', encoding='utf8') as json_file:
            json_data = json.dumps([*all_items.values()], ensure_ascii=False)
            json_file.write(json_data)
            json_file.close()
        pass

def isUrlImage(image_url):
    try:
        r = requests.head(image_url)
        if r.ok and r.headers["content-type"] in isUrlImage.image_formats:
            return True
        return False
    except:
        return False
isUrlImage.image_formats = ("image/png", "image/jpeg", "image/jpg")

def addImageMetadataForItems(items_path):
    counter = 0
    should_run = True
    with open(items_path, encoding='utf8') as json_file:
        data_dict = json.load(json_file)
        json_file.close()
        for item in data_dict:
            if not should_run:
                break
            if 'Image' not in item:
                item['Image'] = findImageOfItem(item['ItemCode'])
            counter = counter + 1
            print(counter)
            if counter%1000 == 0:
                with open(items_path, 'w', encoding='utf8') as json_file:
                    json_data = json.dumps(data_dict, ensure_ascii=False)
                    json_file.write(json_data)
                    json_file.close()
        with open(items_path, 'w', encoding='utf8') as json_file:
            json_data = json.dumps(data_dict, ensure_ascii=False)
            json_file.write(json_data)
            json_file.close()

def findImageOfItem(barcode):
    image = None
    try:
        rami_levy_image = f'https://img.rami-levy.co.il/product/{barcode}/small.jpg'
        if isUrlImage(rami_levy_image):
            image = rami_levy_image 
        else:
            shupersal_url = f'https://www.shufersal.co.il/online/he/search?text={barcode}'
            page = requests.get(shupersal_url)
            tree = html.fromstring(page.content)  
            res = tree.xpath('//*[@id="mainProductGrid"]/li[1]/div[1]/a/img')
            url = res[0].get('src')
            regex = '(f_auto,q_auto\/v)[0-9]*\/'
            url = re.sub(regex,'',url)
            if isUrlImage(url):
                image = url 
    finally:
        return image

def parseNewPrices():
    ramilevy_full = '../data/products/RamiLevyFull.xml'
    shupersal_full = '../data/products/ShupersalFull.xml'
    ramilevy_prices = '../data/products/RamiLevyPrices.xml'
    shupersal_prices = '../data/products/ShupersalPrices.xml'
    all_prices_xml_path = '../data/products/AllPrices.xml'
    json_duplication_path = '../data/products/AllPricesWithDuplication.json'
    json_no_duplication_path = '../data/products/AllPrices.json'
    
    deleteIrelevantRows(ramilevy_full, ramilevy_prices)
    deleteIrelevantRows(shupersal_full, shupersal_prices)

    merge2Prices(ramilevy_prices, shupersal_prices, all_prices_xml_path)
    xml2jsonFile(all_prices_xml_path, json_duplication_path)
    deleteDuplicationItems(json_duplication_path, json_no_duplication_path)
    addImageMetadataForItems(json_no_duplication_path)

def addAllNewProducts(path):
    cred = credentials.Certificate('../../smarttrashcan-credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    with open(path, encoding='utf8') as json_file:
        data_dict = json.load(json_file)
        json_file.close()

        batch = db.batch()
        limit = 490
        counter = 0
        for item in data_dict:
            barcode = int(item['ItemCode'])
            name = item['ItemName']
            source = item['Source']
            image = item['Image']
            batch.set(db.collection('products').document(str(barcode)), {'barcode':barcode, 'name':name, 'source':source, 'image':image})
            counter = counter + 1
            if counter >= limit:
                counter = 0
                batch.commit()
                batch = db.batch()
        batch.commit()

def getNumberOfProducts():
    cred = credentials.Certificate('../../smarttrashcan-credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    snap = db.collection('products').get()
    return len(snap)
    
if __name__ == '__main__':
    path = '../data/products/AllPrices.json'
    parseNewPrices()
    addAllNewProducts(path)
