package com.hansol.eggmoney.ui;

import android.graphics.Color;
import android.graphics.Rect;
import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.Animation;
import android.view.animation.TranslateAnimation;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.hansol.eggmoney.R;
import com.hansol.eggmoney.common.EggMoneyActivity;
import com.hansol.eggmoney.common.EggMoneyPolicy;

import static com.hansol.eggmoney.ui.MainPagerAdapter.TAB_PUBLIC;

public class MainActivity extends EggMoneyActivity {

    private static final String tag = MainActivity.class.getSimpleName();

    private ViewPager pager = null;
    private MainPagerAdapter adapter = null;
    private TextView[] tvTabs = null;
    private LinearLayout llUnderBarContainer = null;
    private ImageView ivUnderBar = null;
    private int left = 0;

    private int currentTabIndex = TAB_PUBLIC;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setBackPressedToast(R.string.toast_backpressed);

        tvTabs = new TextView[MainPagerAdapter.TAB_COUNT];
        tvTabs[MainPagerAdapter.TAB_PUBLIC] = (TextView) findViewById(R.id.tvTabPublic);
        tvTabs[MainPagerAdapter.TAB_EMART] = (TextView) findViewById(R.id.tvTabEmart);
        tvTabs[MainPagerAdapter.TAB_HOMEPLUS] = (TextView) findViewById(R.id.tvTabHomeplus);
        for(TextView tvTab : tvTabs) {
            tvTab.setOnClickListener(onTabClickListener);
        }

        llUnderBarContainer = (LinearLayout) findViewById(R.id.llUnderBarContainer);
        initUnderBar();

        pager = (ViewPager) findViewById(R.id.pager);
        pager.setOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }

            @Override
            public void onPageSelected(int position) {
                updateTabUI(position);
            }

            @Override
            public void onPageScrollStateChanged(int state) {

            }
        });
        adapter = new MainPagerAdapter(this);
        pager.setAdapter(adapter);

        updateTabUI(TAB_PUBLIC);
        pager.setCurrentItem(currentTabIndex);
    }

    private void updateTabUI(int index) {
        for(int i = 0; i < tvTabs.length; i++) {
            tvTabs[i].setSelected(i == index);
        }

        Rect rc = new Rect();
        ivUnderBar.getGlobalVisibleRect(rc);
        int to = (EggMoneyPolicy.getDisplay(this).getWidth() / 3) * index;
        Animation animation = new TranslateAnimation(left, to, 0, 0);
        animation.setDuration(200);
        animation.setFillAfter(true);
        ivUnderBar.startAnimation(animation);
        left = to;

        currentTabIndex = index;
    }

    private View.OnClickListener onTabClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            int index = 0;
            switch (view.getId()) {
                case R.id.tvTabPublic: {
                    index = MainPagerAdapter.TAB_PUBLIC;
                    break;
                }
                case R.id.tvTabEmart: {
                    index = MainPagerAdapter.TAB_EMART;
                    break;
                }
                case R.id.tvTabHomeplus: {
                    index = MainPagerAdapter.TAB_HOMEPLUS;
                    break;
                }
            }
            pager.setCurrentItem(index);
        }
    };

    private void initUnderBar() {
        ivUnderBar = new ImageView(this);
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
        params.width = EggMoneyPolicy.getDisplay(this).getWidth() / 3;
        params.height = EggMoneyPolicy.DPToPixel(this, 3);
        this.ivUnderBar.setBackgroundColor(Color.parseColor("#ffdd60"));
        this.ivUnderBar.setLayoutParams(params);
        this.llUnderBarContainer.addView(this.ivUnderBar);
    }
}
