package com.hansol.eggmoney.common;

import android.content.Context;
import android.view.Display;
import android.view.WindowManager;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class EggMoneyPolicy {

    public static int DPToPixel(Context paramContext, double paramDouble) {
        return (int) (getDestiny(paramContext) * paramDouble + 0.5);
    }

    public static float getDestiny(Context paramContext) {
        return paramContext.getResources().getDisplayMetrics().density;
    }

    public static Display getDisplay(Context paramContext) {
        return ((WindowManager) paramContext.getSystemService("window")).getDefaultDisplay();
    }
}
