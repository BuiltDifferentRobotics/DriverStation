import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class mainRun {
    public static void main(String[] args) throws JSONException {
        JSONObject test = new JSONObject();
        test.append("a", "s");
        jsonParse j = new jsonParse(test);
        packetSend send = new packetSend(8888, j.getJsonString());
        packetReceiver receiver = new packetReceiver(8888);
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        executorService.submit(send);
        executorService.submit(receiver);
    }
}
