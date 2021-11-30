package my;

import java.io.FileWriter;
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import tts_voice.NaverVoiceService;

@Controller
public class MyController {

	@Autowired
	MapService mapservice;
	
	@Autowired
	NaverVoiceService voiceservice;
	
	@RequestMapping("/myinput")
	public String input() {
		return "/my/input";
	}
	@RequestMapping("/myoutput")
	public ModelAndView output(String text) throws IOException{//<form action="/myoutput" <input.. name=""text
		ModelAndView mv = new ModelAndView();
		String response = mapservice.test(text);
		mv.addObject("response", response);
		System.out.println(response);
		
		String filename = "myinput.txt";
		//txt파일 저장=출력
		FileWriter fw = new FileWriter("C:/Users/student/Desktop/images/"+filename);//c:/users/student/Desktp/images/...
		fw.write(response);
		fw.close();
		
		String mp3 = voiceservice.test(filename);
		System.out.println(mp3);
		
		mv.addObject("responsemp3", mp3);
		mv.setViewName("/my/output");
		return mv;
	}
	
	@RequestMapping("/mytotal1")
	public String total1() {
		return "/my/total";
	}
	@RequestMapping("/mytotal2")
	@ResponseBody
	public String total2(String text) throws IOException{
		//$.ajax({ data:{"text":$("#text").val() },,,})
		String response = mapservice.test(text);
		System.out.println(response);
		
		String filename = "myinput.txt";
		//txt파일 저장=출력
		FileWriter fw = new FileWriter("C:/Users/student/Desktop/images/"+filename);//c:/users/student/Desktp/images/...
		fw.write(response);
		fw.close();
		
		String mp3 = voiceservice.test(filename);
		System.out.println(mp3);
		return "{\"response\" : \"" + response + "\"  , \"mp3\" : \"" + mp3 + "\"}";
	}
		
	
}
