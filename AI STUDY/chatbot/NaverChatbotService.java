package chatbot;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
//안드로이드 api를 jdk api로 변경
import java.util.Base64;//암호화
import java.util.Date;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.stereotype.Service;

import edu.spring.naverai.NaverService;
@Service
public class NaverChatbotService implements NaverService {
	//voiceMessage  질문 , 답변 리턴
	public String test(String voiceMessage) {
		return test(voiceMessage, "send");
	}
  public String test(String voiceMessage, String event) {//send/open

	  	String apiURL = "https://c89f948456fa4269a4f1d641a4dfb90f.apigw.ntruss.com/custom/v1/5515/1c7f45ba1553474dc67c6c5348c2a6ff0e1b59a4e54e64eed364aaaaf5b37770";
        String secretKey = "bGNJSlF3a2RrcHBMSG5MSHR4d1JPT096VVVpcklYdUw=";
        
	  	String chatbotMessage = "";

        try {
            URL url = new URL(apiURL);

            String message = getReqMessage(voiceMessage, event);
            //메소드 내부 출력 - 현재 시각 1/1000초 단위 출력 ##1633401235875
            
            System.out.println("##" + message);
            //##{"bubbles":[{"data":{.... - 질문 

            String encodeBase64String = makeSignature(message, secretKey);

            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json;UTF-8");
            con.setRequestProperty("X-NCP-CHATBOT_SIGNATURE", encodeBase64String);

            // post request
            con.setDoOutput(true);
            DataOutputStream wr = new DataOutputStream(con.getOutputStream());
            wr.write(message.getBytes("UTF-8"));
            wr.flush();
            wr.close();
            int responseCode = con.getResponseCode();

            BufferedReader br;

            if(responseCode==200) { // Normal call
                System.out.println(con.getResponseMessage());//ok(챗봇서버 대화응답)

                BufferedReader in = new BufferedReader(
                        new InputStreamReader(
                                con.getInputStream()));
                String decodedString;
                while ((decodedString = in.readLine()) != null) {
                    chatbotMessage = decodedString;
                }
                //chatbotMessage = decodedString;
                in.close();

            } else {  // Error occurred
                chatbotMessage = con.getResponseMessage();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println("서비스출력=" + chatbotMessage);
        return chatbotMessage;
    }

    public static String makeSignature(String message, String secretKey) {

        String encodeBase64String = "";

        try {
            byte[] secrete_key_bytes = secretKey.getBytes("UTF-8");

            SecretKeySpec signingKey = new SecretKeySpec(secrete_key_bytes, "HmacSHA256");
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(signingKey);

            byte[] rawHmac = mac.doFinal(message.getBytes("UTF-8"));
           // encodeBase64String = Base64.encodeToString(rawHmac, Base64.NO_WRAP);
            encodeBase64String = Base64.getEncoder().encodeToString(rawHmac);
            return encodeBase64String;

        } catch (Exception e){
            System.out.println(e);
        }

        return encodeBase64String;

    }

    public static String getReqMessage(String voiceMessage, String event) {
    	//질문을  json형태 생성

        String requestBody = "";

        try {

            JSONObject obj = new JSONObject();

            long timestamp = new Date().getTime();

            System.out.println("##"+timestamp);//##1633401235875

            obj.put("version", "v2");
            obj.put("userId", "U47b00b58c90f8e47428af8b7bddc1231heo2");
//=> userId is a unique code for each chat user, not a fixed value, recommend use UUID. use different id for each user could help you to split chat history for users.

            obj.put("timestamp", timestamp);

            JSONObject bubbles_obj = new JSONObject();

            bubbles_obj.put("type", "text");

            JSONObject data_obj = new JSONObject();
            data_obj.put("description", voiceMessage);//질문내용

            bubbles_obj.put("type", "text");
            bubbles_obj.put("data", data_obj);

            JSONArray bubbles_array = new JSONArray();
            bubbles_array.put(bubbles_obj);

            obj.put("bubbles", bubbles_array);
            obj.put("event", event);// 웰컴메시지(기본답변) / json 질문- json 답변( 기본, 이미지, 멀티링크 답변)
            //obj.put("event", "open");//웰컴메시지
            //obj.put("event", "getPersistentMenu");//고정메뉴
            
            requestBody = obj.toString();

        } catch (Exception e){
            System.out.println("## Exception : " + e);
        }

        return requestBody;

    }
}

