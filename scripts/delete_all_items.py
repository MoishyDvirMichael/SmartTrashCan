import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys

cred = credentials.Certificate('../data/smarttrashcan-credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


batch_size = 100

coll_ref = db.collection('users').document(sys.argv[1]).collection('scanned_products')
delete_collection(coll_ref, batch_size)

coll_ref = db.collection('users').document(sys.argv[1]).collection('archived_products')
delete_collection(coll_ref, batch_size)
