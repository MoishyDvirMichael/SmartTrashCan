import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from my_application import MyApplication

db = None

def init():
    cred = credentials.Certificate('../data/smarttrashcan-credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()




if __name__=='__main__':
    # init()
    app = MyApplication()
    app.run()
    # while True:
    #     barcode = input('Scan a barcode\n')
    #     print(f'{barcode} was scanned')
    #     doc_ref = db.collection('users').document('moishy').collection('scanned_products')
    #     doc_ref.add({
    #         'barcode': barcode,
    #         'is_identified': False,
    #         #'date_added': firestore.SERVER_TIMESTAMP
    #     })
    #     time.sleep(1)