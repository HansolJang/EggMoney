package com.hansol.eggmoney.ui;

import android.content.Context;
import android.view.View;

import com.hansol.eggmoney.R;
import com.hansol.eggmoney.common.EggMoneyView;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class EmartView extends EggMoneyView {

    private static final String tag = EmartView.class.getSimpleName();

    public EmartView(Context context) {
        super(context);
        View view = inflate(context, R.layout.view_emart, this);
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
