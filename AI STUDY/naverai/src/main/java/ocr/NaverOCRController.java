package ocr;

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
public class NaverOCRController {
	@Autowired
	NaverOCRService ocrservice;

	@RequestMapping("/ocrinput")
	public ModelAndView faceinput() {
		System.out.println("컨트롤러");
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/ocr/ocrinput");
		return mv;

	}
	@RequestMapping("/ocr")
	public ModelAndView face(String image){// 이미지파일명
		System.out.println("시작");
		String jsonModel = "";
		jsonModel = ocrservice.test(image);//  이미지파일명
		ModelAndView mv = new ModelAndView();
		mv.addObject("ocrresult", jsonModel);//텍스트추출json
		mv.setViewName("/ocr/ocr");
		return mv;
		
	}
	
}
