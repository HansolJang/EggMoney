package com.hansol.eggmoney.http.json;

/**
 * Created by zipdoc on 2017. 1. 31..
 */

public class JSEgg {

    String customer_price;
    String date;
    String product_title;
    String product_url;
    String retail_price;
    String wholesale_price;

    public String getCustomer_price() {
        return this.customer_price;
    }

    public String getDate() {
        return this.date;
    }

    public String getProduct_title() {
        return this.product_title;
    }

    public String getProduct_url() {
        return this.product_url;
    }

    public String getRetail_price() {
        return this.retail_price;
    }

    public String getWholesale_price() {
        return this.wholesale_price;
    }
}
