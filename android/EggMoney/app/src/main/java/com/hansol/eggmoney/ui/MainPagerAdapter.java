package com.hansol.eggmoney.ui;

import android.content.Context;
import android.os.Handler;
import android.support.v4.view.PagerAdapter;
import android.view.View;
import android.view.ViewGroup;

import com.hansol.eggmoney.common.EggMoneyView;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class MainPagerAdapter extends PagerAdapter {

    private static final String tag = MainPagerAdapter.class.getSimpleName();

    public static final int TAB_COUNT = 3;
    public static final int TAB_PUBLIC = 0;
    public static final int TAB_EMART = 1;
    public static final int TAB_HOMEPLUS = 2;

    private Context context = null;
    private Handler handler = null;
    private EggMoneyView[] items = null;

    public MainPagerAdapter(Context context) {
        this.context = context;
        this.handler = new Handler();
        items = new EggMoneyView[TAB_COUNT];
        items[TAB_PUBLIC] = new PublicView(context);
        items[TAB_EMART] = new EmartView(context);
        items[TAB_HOMEPLUS] = new HomeplusView(context);
    }

    @Override
    public int getCount() {
        return TAB_COUNT;
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        EggMoneyView content = items[position % TAB_COUNT];
        container.addView(content);
        return content;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView((View) object);
    }

    public void refresh(int index) {
        if(index < TAB_COUNT && items[index] != null) {
            items[index].onUpdateView(null);
        }
    }
}
