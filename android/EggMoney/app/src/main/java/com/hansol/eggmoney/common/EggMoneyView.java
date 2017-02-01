package com.hansol.eggmoney.common;

import android.content.Context;
import android.util.AttributeSet;
import android.widget.LinearLayout;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public abstract class EggMoneyView extends LinearLayout {

    private static final String tag = EggMoneyView.class.getSimpleName();
    private Context context = null;

    public EggMoneyView(Context context) {
        super(context);
        onInitView();
    }

    public EggMoneyView(Context context, AttributeSet attrs) {
        super(context, attrs);
        onInitView();
    }

    public EggMoneyView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        onInitView();
    }

    protected abstract void onInitView();

    public abstract void onReleaseView();

    public abstract void onUpdateView(Object paramObject);

}
