package cfr;

import java.io.File;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class NaverFaceController {
	@Autowired
	NaverFaceService faceservice;
	
	@Autowired
	NaverFaceService2 faceservice2;
	
	@RequestMapping("/faceinput")
	public ModelAndView faceinput() {
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/cfr/faceinput");
		return mv;
		/*for(String one : namelist) {
			//namelist  파일이고 확장자 jpg tfif png 
			System.out.println(one);
		}*/
	
	}
	
	@RequestMapping("/face")
	public ModelAndView face(String image) {
		System.out.println("시작");
		ModelAndView mv = new ModelAndView();
		String jsonModel = faceservice.test(image);
		mv.addObject("faceresult", jsonModel);
		mv.setViewName("/cfr/face");
		//cfr/face.jsp -- ${param.image} <%=request.getParameter("image")%>
		return mv;
		
	}
	
	@RequestMapping("/faceinput2")
	public ModelAndView faceinput2() {
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/Users/student/Desktop/images");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/cfr/faceinput2");
		return mv;
		/*for(String one : namelist) {
			//namelist  파일이고 확장자 jpg tfif png 
			System.out.println(one);
		}*/
	
	}
	@RequestMapping("/face2")
	public ModelAndView face2(String image) {//request.getParameter("image")
		ModelAndView mv = new ModelAndView();
		String jsonModel = faceservice2.test(image);//얼굴감지
		mv.addObject("faceresult2", jsonModel);
		//mv.setViewName("/cfr/face2");
		mv.setViewName("cfr/face2_canvas");
		return mv;
	}
	
}
