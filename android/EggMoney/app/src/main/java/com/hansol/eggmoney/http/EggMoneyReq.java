package com.hansol.eggmoney.http;

import com.hansol.eggmoney.http.json.JSEggList;

import retrofit2.Call;
import retrofit2.http.GET;

/**
 * Created by zipdoc on 2017. 1. 31..
 */

public abstract interface EggMoneyReq {

    @GET("emart")
    public abstract Call<JSEggList> getEmartList();

    @GET("homeplus")
    public abstract Call<JSEggList> getHomeplusList();

    @GET("main")
    public abstract Call<JSEggList> getPublicList();

}
