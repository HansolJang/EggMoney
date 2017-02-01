package com.hansol.eggmoney;

import android.app.Activity;
import android.app.Application;
import android.content.Context;
import android.util.Log;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.Writer;

/**
 * Created by zipdoc on 2017. 2. 1..
 */

public class EggMoney extends Application {

    private static volatile Activity currentActivity = null;
    private static EggMoney instance;
    private static final String tag = EggMoney.class.getSimpleName();
    private Thread.UncaughtExceptionHandler mUncaughtExceptionHandler;

    public static Activity getCurrentActivity() {
        return currentActivity;
    }

    public static EggMoney getGlobalApplicationContext() {
        if (instance == null) {
            throw new IllegalStateException("this application does not inherit GlobalApplication");
        }
        return instance;
    }

    private String getStackTrace(Throwable th) {

        final Writer result = new StringWriter();
        final PrintWriter printWriter = new PrintWriter(result);

        Throwable cause = th;
        while (cause != null) {
            cause.printStackTrace(printWriter);
            cause = cause.getCause();
        }
        final String stacktraceAsString = result.toString();
        printWriter.close();

        return stacktraceAsString;
    }

    private void initRuntimeValues() {
        //init storage
    }

    public static void setCurrentActivity(Activity paramActivity) {
        currentActivity = paramActivity;
    }

    protected void attachBaseContext(Context paramContext) {
        super.attachBaseContext(paramContext);
    }

    public void onCreate() {
        super.onCreate();

        Log.d(tag, "onCreate");

        mUncaughtExceptionHandler = Thread.getDefaultUncaughtExceptionHandler();
        Thread.setDefaultUncaughtExceptionHandler(new UncaughtExceptionHandlerApplication());

        initRuntimeValues();
//        initImageLoader(this);
        instance = this;
    }

    public void onTerminate() {
        super.onTerminate();
        Log.d(tag, "onTerminate");
    }

    private class UncaughtExceptionHandlerApplication implements Thread.UncaughtExceptionHandler{

        @Override
        public void uncaughtException(Thread thread, Throwable ex) {

            String error = getStackTrace(ex);
            /*
            PendingIntent intent = PendingIntent.getActivity(getApplicationContext(),
                    192837, new Intent(getApplicationContext(), BugReportActivity.class),
                    PendingIntent.FLAG_ONE_SHOT);

            AlarmManager alarmManager;
            alarmManager = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
            alarmManager.set(AlarmManager.ELAPSED_REALTIME_WAKEUP,
                    1000, intent);
            */

//            Intent intent = new Intent(getApplicationContext(), BugReportActivity.class);
//            if (error.length() > 4096) {
//                error = error.substring(0, 4096);
//            }
//
//            intent.putExtra("stack_trace", error);
//            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//            startActivity(intent);


            android.os.Process.killProcess(android.os.Process.myPid());
            System.exit(2);

            //mUncaughtExceptionHandler.uncaughtException(thread, ex);
        }
    }
}
