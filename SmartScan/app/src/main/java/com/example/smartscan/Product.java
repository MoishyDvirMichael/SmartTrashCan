package com.example.smartscan;

import com.google.firebase.firestore.DocumentReference;

import java.util.Date;

public class Product {
    private String barcode;
    private Date date_added;
    private Boolean is_identified;
    private DocumentReference product;

    public Product(){}
    public Product(String code, Date date, Boolean is_identified, DocumentReference ref){
        this.barcode = code;
        this.date_added = date;
        this.is_identified = is_identified;
        this.product = ref;
    }

    public String getBarcode() {
        return barcode;
    }

    public void setBarcode(String barcode) {
        this.barcode = barcode;
    }

    public Boolean getIs_identified() {
        return is_identified;
    }

    public void setIs_identified(Boolean is_identified) {
        this.is_identified = is_identified;
    }

    public DocumentReference getProduct() {
        return product;
    }

    public void setProduct(DocumentReference product) {
        this.product = product;
    }

    public Date getDate_added() {
        return date_added;
    }

    public void setDate_added(Date date_added) {
        this.date_added = date_added;
    }
}
