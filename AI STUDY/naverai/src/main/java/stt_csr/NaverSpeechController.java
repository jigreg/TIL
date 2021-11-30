package stt_csr;

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
public class NaverSpeechController {
	@Autowired
	NaverSpeechService speechservice;

	@RequestMapping("/speechinput")
	public ModelAndView faceinput() {
		System.out.println("컨트롤러");
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/stt_csr/speechinput");
		return mv;

	}
	@RequestMapping("/speech")
	public ModelAndView face(String image, String lang) 
	throws IOException{//mp3
		System.out.println("시작");
		String jsonModel = "";
		if(lang == null) {
			jsonModel = speechservice.test(image);
		}
		else {
			jsonModel = speechservice.test(image, lang);
		}
		ModelAndView mv = new ModelAndView();
		mv.addObject("speechresult", jsonModel);
		// 파일 저장///////////////////////////
		//1.json 파싱
		JSONObject obj = new JSONObject(jsonModel);
		String text = (String)obj.get("text");
		//2.파일명 현재시각
		SimpleDateFormat sf = new SimpleDateFormat("yyyyMMddHHmmss");
		String filename = sf.format(new Date());
		//3.출력
		FileWriter fw = new FileWriter
				("C:/Users/student/Desktop/images/"+filename+".txt", true);
		fw.write(text+"\n");
		fw.close();
		///////////////////////////////////
		mv.setViewName("/stt_csr/speech");
		return mv;
		
	}
	
}
