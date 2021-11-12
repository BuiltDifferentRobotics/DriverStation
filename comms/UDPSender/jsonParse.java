import org.json.JSONObject;
import org.json.*;
import org.json.JSONString;

import java.util.HashMap;


public class jsonParse {
    private JSONObject jsonmsg;
    private String jsonString;
    public jsonParse(JSONObject message){
        this.jsonmsg = message;
        this.jsonString = this.jsonmsg.toString();
    }

    public JSONObject getJsonmsg() {
        return jsonmsg;
    }

    public String getJsonString() {
        return jsonString;
    }
}

