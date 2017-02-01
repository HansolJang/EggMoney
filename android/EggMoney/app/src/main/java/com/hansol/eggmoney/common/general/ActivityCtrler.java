package com.hansol.eggmoney.common.general;

import android.app.Activity;
import android.widget.Toast;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class ActivityCtrler {

    private long backKeyPressedTime = 0L;
    private Activity activity = null;
    private int res = 0;

    public ActivityCtrler(Activity activity, int res) {
        this.activity = activity;
        this.res = res;
    }

    public boolean onBackPressed() {
        if(System.currentTimeMillis() <= this.backKeyPressedTime) {
            this.activity.finish();
            return true;
        } else {
            this.backKeyPressedTime = System.currentTimeMillis() + 3000L;
            Toast.makeText(this.activity, this.activity.getResources().getString(this.res), 0).show();
            return false;
        }
    }
}
