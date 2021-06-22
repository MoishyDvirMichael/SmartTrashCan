import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from consts import Consts
from timeout import timeout

class DB:
    @classmethod
    def init(cls):
        cred = credentials.Certificate('../data/smarttrashcan-credentials.json')
        firebase_admin.initialize_app(cred)
        cls.db = firestore.client()
    
    @classmethod
    def add_scanned_item(cls, uid, barcode, callback):
        try:
            return cls.__add_scanned_item(uid, barcode, callback)
        except:
            return None

    @classmethod
    @timeout(Consts.DATABASE_TIMEOUT)
    def __add_scanned_item(cls, uid, barcode, callback):
        doc_ref = cls.db.collection('users').document(uid).collection('scanned_products')
        doc_id = doc_ref.add({
            'barcode': barcode,
            'date_added': firestore.SERVER_TIMESTAMP
        })

        doc_ref = cls.db.collection('users').document(uid).collection('scanned_products').document(doc_id[1].id)
        doc_watch = doc_ref.on_snapshot(callback)
        return doc_watch

    @classmethod
    def get_product(cls, doc_ref):
        try:
            doc = doc_ref.get()
            return doc._data
        except:
            return None

    @classmethod
    def get_recycling_bin_type(cls, doc_ref):
        try:
            if doc_ref == None:
                return Consts.DEFAULT_RECYCLING_BIN_TYPE
            doc = doc_ref.get()
            recycling_bin_type = doc._data
            recycling_bin_type['color_hex'] = Consts.convert_color_to_tkinter(recycling_bin_type.get('color_hex'))
            return recycling_bin_type
        except:
            return Consts.DEFAULT_RECYCLING_BIN_TYPE