package com.builtdifferent.udpServerTesting;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class mainRun {
    public static void main(String[] args) throws JSONException {
        JSONObject test = new JSONObject();
        test.append("test", "Satyansh");
        jsonParse j = new jsonParse(test);
        PacketSend send = new PacketSend(1156, j.getJsonString());
        PacketReciever receiver = new PacketReciever(8888);
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        executorService.submit(send);
        executorService.submit(receiver);
    }
}