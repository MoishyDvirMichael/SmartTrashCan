import * as functions from 'firebase-functions';
import { firestore } from 'firebase-admin';
import * as admin from 'firebase-admin';

admin.initializeApp();

export const findDataForBarcode = functions.firestore.document('/users/{user}/scanned_products/{documentId}')
    .onCreate(async (snap, context) => {
        const data = snap.data();
        const barcode = data.barcode;

        let new_data: any = {is_checked: false};
        
        const product = await getDocument(admin.firestore().collection('products').where('barcode', '==', barcode).limit(1));
        if (product !== null) {
            new_data.product_id = product;
            new_data.is_identified = true;
        }
        else {
            new_data.is_identified = false;
        }
        await snap.ref.set(new_data, { merge: true });
    });

async function getDocument(doc_ref: firestore.Query) {
    const snap = await doc_ref.get();
    if (snap.empty) {
        return null;
    } else {
        return snap.docs[0].ref;
    }
}

// const db = admin.firestore();
// initializeDatabase();

// export const addBarcode = functions.https.onRequest(async (req, res) => {
//     const barcode :number=parseInt(req.query.barcode!.toString());
//     const data = {
//         barcode: barcode,
//         // is_identified: false,
//         date_added: admin.firestore.Timestamp.now(),
//     };
//     const writeResult = await db.collection('users/moishy/scanned_products').add(data);
//     res.json({ result: `Message with ID: ${writeResult.id} added.` });
// });

// async function initializeDatabase() {
//     await db.doc('recycling_bin_types/bOmcWUdCQpEdKhtLREeP').set({color_hex: "0x808080", color_name: "gray", name: "metal"});
//     await db.collection('products').add({barcode:7290011447304, image: "https://img.rami-levy.co.il/product/7290011447304/small.jpg", name: "תחליף חלב חלבי שלב 3", recycling_bin_type: '/recycling_bin_types/bOmcWUdCQpEdKhtLREeP', source: "Rami Levy"});
//     // await db.collection('users/moishy/scanned_products').add({barcode: 7290011447304, is_identified: false, date_added: admin.firestore.Timestamp.now()});
//     // let writeResult = await db.collection('recycling_bin_types').where('name', '==', 'unknown').get();
//     // await db.collection('users/moishy/scanned_products').add({barcode:7290000060576, date_added: admin.firestore.FieldValue.serverTimestamp()})
// }