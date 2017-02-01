package com.hansol.eggmoney;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

import com.hansol.eggmoney.common.EggMoneyActivity;
import com.hansol.eggmoney.ui.MainActivity;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class IntroActivity extends EggMoneyActivity {

    private static final String tag = IntroActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_intro);

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                IntroActivity.this.finish();
                Intent intent = new Intent(IntroActivity.this, MainActivity.class);
                startActivity(intent);
            }
        }, 2000);
    }
}
