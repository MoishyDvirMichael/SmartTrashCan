
import * as functions from 'firebase-functions';

import { firestore } from 'firebase-admin';
import * as admin from 'firebase-admin';
// import * as puppeteer from 'puppeteer';
import { Product } from './Product';

admin.initializeApp();
// const db = admin.firestore();
// let unknownRecyclingBinType: firestore.DocumentReference<firestore.DocumentData>;
// initializeDatabase();

// export const addBarcode = functions.https.onRequest(async (req, res) => {
//     const barcode = req.query.barcode;
//     const data = {
//         barcode: barcode,
//         is_identified: false,
//         date_added: admin.firestore.Timestamp.now(),
//     };
//     const writeResult = await db.collection('users/moishy/scanned_products').add(data);
//     res.json({ result: `Message with ID: ${writeResult.id} added.` });
// });

export const findDataForBarcode = functions.firestore.document('/users/{user}/scanned_products/{documentId}')
    .onCreate(async (snap, context) => {
        const data = snap.data();
        const barcode = data.barcode;
        let is_identified;
        let product_id = null;

        const product = await getDocument(admin.firestore().collection('products').where('barcode', '==', barcode).limit(1));
        if (product !== null) {
            product_id = product;
            is_identified = true;
        }
        else {
            // const new_product = await scrapeProduct(barcode);
            const new_product = null;
            if (new_product !== null) {
                product_id = await addNewProduct(new_product);
                is_identified = true;
            } else {
                is_identified = false;
            }
        }
        await snap.ref.set({ is_identified, product: product_id, is_checked: false }, { merge: true });
    });

async function getDocument(doc_ref: firestore.Query) {
    const snap = await doc_ref.get();
    if (snap.empty) {
        return null;
    } else {
        return snap.docs[0].ref;
    }
}

async function addNewProduct(product: Product) {
    const res = await admin.firestore().collection('products').add(product);
    return res;
}

// async function scrapeProduct(barcode: number) {
//     const url = `https://www.rami-levy.co.il/he/shop?item=${barcode}`;
//     const browser = await puppeteer.launch();
//     let return_value = null;
//     try {
//         const page = await browser.newPage();
//         await page.goto(url);
//
//         const raw_image = await page.$eval('.product-img.mt-5', (e) => e.outerHTML);
//         const images_url = raw_image.split('&quot;');
//         if (images_url.length != 3) {
//             throw `Can't find image in ${url}`;
//         }
//         const image_url = images_url[1];
//         const name = await page.$eval('.h2.mt-4.mt-md-0', (e) => e.innerHTML);
//         const images = [image_url];
//         const recycling_bin_type = unknownRecyclingBinType;
//         return_value = {
//             barcode,
//             name,
//             images,
//             recycling_bin_type,
//         };
//     } finally {
//         browser.close();
//         return return_value;
//     }
// }

// async function initializeDatabase() {
//     let writeResult = await db.collection('recycling_bin_types').where('name', '==', 'unknown').get();
//     unknownRecyclingBinType = writeResult.docs[0].ref;
// }