package com.hansol.eggmoney.http.json;

import java.util.List;

/**
 * Created by zipdoc on 2017. 1. 31..
 */

public class JSEggList {

    List<JSEgg> rows;
    String title;

    public List<JSEgg> getRows() {
        return this.rows;
    }

    public String getTitle() {
        return this.title;
    }
}
