package pose;

import java.io.File;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class NaverPoseController {
	@Autowired
	NaverPoseService poseservice;

	@RequestMapping("/poseinput")
	public ModelAndView faceinput() {
		System.out.println("컨트롤러");
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/pose/poseinput");
		return mv;

	}
	//http://localhost:9002/objectdetection?image=computer.jpg
	@RequestMapping("/pose")
	public ModelAndView face(String image) {
		System.out.println("시작");
		ModelAndView mv = new ModelAndView();
		String jsonModel = poseservice.test(image);
		mv.addObject("poseresult", jsonModel);
		mv.setViewName("/pose/pose");
		return mv;
		
	}
	
}
