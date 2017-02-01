package com.hansol.eggmoney.ui;

import android.content.Context;
import android.view.View;

import com.hansol.eggmoney.R;
import com.hansol.eggmoney.common.EggMoneyView;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class HomeplusView extends EggMoneyView {

    private static final String tag = HomeplusView.class.getSimpleName();

    public HomeplusView(Context context) {
        super(context);
        View view = inflate(context, R.layout.view_homeplus, this);
    }

    @Override
    protected void onInitView() {

    }

    @Override
    public void onReleaseView() {

    }

    @Override
    public void onUpdateView(Object paramObject) {

    }
}
