package tts_voice;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class NaverVoiceController {
	@Autowired
	NaverVoiceService voiceservice;

	@RequestMapping("/voiceinput")
	public ModelAndView faceinput() {
		System.out.println("컨트롤러");
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/tts_voice/voiceinput");
		return mv;

	}
	@RequestMapping("/voice")
	public ModelAndView face(String text, String speaker)// txt파일명 , jinho 
	throws IOException{
		System.out.println("시작");
		String mp3file = "";
		mp3file = voiceservice.test(text, speaker);//  공백이면 정상실행(xxxx.mp3파일 생성) , 아니면 오류 
		ModelAndView mv = new ModelAndView();
		mv.addObject("voiceresult", mp3file);

		mv.setViewName("/tts_voice/voice");
		return mv;
		
	}
	
}
