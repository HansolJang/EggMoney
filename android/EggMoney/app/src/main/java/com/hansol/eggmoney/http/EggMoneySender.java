package com.hansol.eggmoney.http;

import android.content.Context;

import com.hansol.eggmoney.R;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class EggMoneySender {

    public static EggMoneyReq getSender(Context context, int server_id) {
        return new Retrofit.Builder()
                .baseUrl(context.getString(server_id))
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(EggMoneyReq.class);
    }

}
