package com.hansol.eggmoney.common.general;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v4.content.LocalBroadcastManager;
import android.util.Log;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class Activity_ extends FragmentActivity {
    private static final String tag = Activity_.class.getSimpleName();
    private ActivityCtrler activityCtrler = null;
    private boolean br_flag = false;
    private int backPressedToastRes = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

//        try {
//            ActivityStack stack = ActivityStack.getInstance(ActivityStack.class);
//            stack.addStack(this);
//        } catch (Exception e) {
//        }
    }

    protected void onFinish() { }

    @Override
    protected void onDestroy() {
        if(br_flag) {
            unregisterBroadcastReceiver();
        }
//        try {
//            ActivityStack stack = ActivityStack.getInstance(ActivityStack.class);
//            stack.remStack(this);
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
        super.onDestroy();
    }

    private static final String action_name = Activity_.class.getSimpleName();
    protected void registerBroadcastReceiver() {
        IntentFilter filter = new IntentFilter();
        filter.addAction(action_name);
        LocalBroadcastManager.getInstance(this).registerReceiver(onListener, filter);
        br_flag = true;
    }

    protected void unregisterBroadcastReceiver() {
        LocalBroadcastManager.getInstance(this).unregisterReceiver(onListener);
        br_flag = false;
    }

    private BroadcastReceiver onListener = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if(action.equals(action_name)) {
                Bundle bundle = intent.getExtras();
                if(bundle != null)
                    onBroadcastReceiver(intent);
            }
        }
    };

    protected void onBroadcastReceiver(Intent intent) {}

    public boolean sendBroadcastReceiver(Intent intent) {
        boolean result = LocalBroadcastManager.getInstance(Activity_.this).sendBroadcast(intent);
        Log.d(tag, "sendBroadcastReceiver : " + result);
        return result;
    }

    public static boolean sendBroadcastReceiver(Context context, Intent intent) {
        boolean result = LocalBroadcastManager.getInstance(context).sendBroadcast(intent);
        Log.d(tag, "sendBroadcastReceiver : " + result);
        return result;
    }

    public static Intent NEW_DEFAULT_INTENT() {
        return new Intent(action_name);
    }

    public static Intent NEW_DEFAULT_INTENT(String key, String value) {
        Intent intent = NEW_DEFAULT_INTENT();
        intent.putExtra(key, value);
        return intent;
    }

    public static Intent NEW_DEFAULT_INTENT(Intent src) {
        Intent intent = NEW_DEFAULT_INTENT();
        Bundle bundle = intent.getExtras();
        if(bundle != null) {
            for(String key : bundle.keySet()) {
                Object value = bundle.get(key);
                intent.putExtra(key, value.toString());
            }
        }
        return intent;
    }

    @Override
    public void onBackPressed() {
        if(activityCtrler != null) {
            boolean flag = activityCtrler.onBackPressed();
            Log.d(tag, "onBackPressed() : " + flag);
            if(flag) {
                onFinish();
            }
        } else {
            super.onBackPressed();
        }
    }

    protected void setBackPressedToast(int backPressedToastRes) {
        activityCtrler = null;
        this.backPressedToastRes = backPressedToastRes;
        if(this.backPressedToastRes != 0)
            activityCtrler = new ActivityCtrler(this, backPressedToastRes);
    }

}
