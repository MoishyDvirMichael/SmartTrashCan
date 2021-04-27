import { firestore } from "firebase-admin";

export interface Product {
    barcode: number,
    name: string,
    images: string[],
    recycling_bin_type?: firestore.DocumentReference,
}