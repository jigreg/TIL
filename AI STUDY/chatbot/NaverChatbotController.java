package chatbot;

import java.io.File;
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
/*
@Service
public class NaverChatbotService implements NaverService

@Service("voiceservice")
public class NaverChatbotVoiceService implements NaverService 

스프링해석 
NaverChatbotVoiceService   voiceservice = new NaverChatbotVoiceService();
NaverChatbotService  naverService = new NaverChatbotService();
*/

@Controller
public class NaverChatbotController {

	@Autowired
	NaverChatbotService chatbotservice;
	
	@Autowired
	@Qualifier("voiceservice")
	NaverChatbotVoiceService voiceservice;//텍스트를 음성답변 변환 필요
	
	@Autowired
	@Qualifier("speechservice")
	NaverChatbotSpeechService speechservice;//음성질문을 텍스트변환-챗봇질문입력 필요
	
	
	@RequestMapping("/chatbotstart")
	public String chatbotstart() {
		return "/chatbot/chatbotstart";
	}
	
	@RequestMapping("/chatbot")
	@ResponseBody
	public String chatbot(String message) {//뷰 입장버튼 클릭시(질문입력이전. 즉, message="")
		String event = null;
		if(message == "") {
			event = "open";
		}
		else {
			event = "send";
		}
		String response =  chatbotservice.test(message, event);
		System.out.println("컨트롤러출력="+response);
		return response;//답변
	}
	
	@RequestMapping("/chatbotvoice")
	@ResponseBody
	public String voice(String text) {
		String mp3file = voiceservice.test(text);
		return mp3file;
	}
	
	//1.클라이언트 컴퓨터 녹음파일로 저장(jsp)-mictest.html 참고
	//2. 스프링부트 서버 컴퓨터 업로드 url - 처리
	@RequestMapping(value="/mp3upload", method = RequestMethod.POST)
	@ResponseBody
	public String upload(MultipartFile file) throws IOException {
		System.out.println(file.getOriginalFilename());
		//업로드한 파일명 추출
		String filename = file.getOriginalFilename();
		//c:바탕화면/images/*.* 저장
		String savePath = "C:/Users/student/Desktop/images/";
		File saveFile = new File(savePath + filename);
		file.transferTo(saveFile);//
		return "잘 받았습니다.";

	}
	
	//3. 2번 mp3  파일을 speechservice에게 전달하여 결과 텍스트 리턴
	@RequestMapping("/chatbotspeech")
	@ResponseBody	
	public String speech(String filename){
		String text = speechservice.test(filename);
		return text;
	}
	
	   
}





