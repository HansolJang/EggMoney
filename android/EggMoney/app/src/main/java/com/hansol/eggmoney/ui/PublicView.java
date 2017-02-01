package com.hansol.eggmoney.ui;

import android.content.Context;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.hansol.eggmoney.R;
import com.hansol.eggmoney.common.EggMoneyView;
import com.hansol.eggmoney.http.EggMoneyReq;
import com.hansol.eggmoney.http.EggMoneySender;
import com.hansol.eggmoney.http.json.JSEggList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class PublicView extends EggMoneyView {

    private static final String tag = PublicView.class.getSimpleName();

    private Context context = null;

    public PublicView(Context context) {
        super(context);
        this.context = context;
        View view = inflate(context, R.layout.view_public, this);

        doPublic();
    }

    @Override
    protected void onInitView() {

    }

    @Override
    public void onReleaseView() {

    }

    @Override
    public void onUpdateView(Object paramObject) {
        doPublic();
    }

    private void doPublic() {
        EggMoneyReq sender = EggMoneySender.getSender(context, R.string.server_url);
        sender.getPublicList().enqueue(new Callback<JSEggList>() {
            @Override
            public void onResponse(Call<JSEggList> call, Response<JSEggList> response) {
                if(response.isSuccessful()) {
                    Log.d(tag, response.body() + "");
                }
            }

            @Override
            public void onFailure(Call<JSEggList> call, Throwable t) {
                Toast.makeText(context, context.getString(R.string.result_none) + ": " + t.getMessage(), Toast.LENGTH_SHORT).show();
                showErrorLayout(true);
            }
        });
    }

    private void showErrorLayout(boolean error) {

    }
}
