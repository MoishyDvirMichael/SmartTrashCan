import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class DB:
    @classmethod
    def init(cls):
        cred = credentials.Certificate('../data/smarttrashcan-credentials.json')
        firebase_admin.initialize_app(cred)
        cls.db = firestore.client()
    
    @classmethod
    def add_scanned_item(cls, barcode, callback):
        # doc_ref = cls.db.collection('users').document('moishy').collection('scanned_products')
        doc_ref = cls.db.collection('recycling_bin_types')
        doc_id = doc_ref.add({
            'barcode': barcode,
            # 'is_identified': False,
            'date_added': firestore.SERVER_TIMESTAMP
        })

        # doc_ref = cls.db.collection('users').document('moishy').collection('scanned_products').document(doc_id)
        doc_ref = cls.db.collection('recycling_bin_types').document(doc_id[1].id)
        doc_watch = doc_ref.on_snapshot(callback)
        return doc_watch

        
