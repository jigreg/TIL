package objectdetection;

import java.io.File;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class NaverObjectDetectionController {
	@Autowired
	NaverObjectDetectionService odservice;

	@RequestMapping("/objectdetectioninput")
	public ModelAndView faceinput() {
		//이미지파일 리스트 모델 생성 - 뷰 전달
		//C:\Users\student\Desktop\images  폴더 파일명 리스트 
		File f = new File("C:/kdigital2/images/");
		String[] namelist = f.list();
		ModelAndView mv = new ModelAndView();
		mv.addObject("filelist", namelist);
		mv.setViewName("/od/objectdetectioninput");
		return mv;
		/*for(String one : namelist) {
			//namelist  파일이고 확장자 jpg tfif png 
			System.out.println(one);
		}*/
	
	}
	
	@RequestMapping("/objectdetection")
	public ModelAndView face(String image) {
		System.out.println("시작");
		ModelAndView mv = new ModelAndView();
		String jsonModel = odservice.test(image);
		mv.addObject("odresult", jsonModel);
		mv.setViewName("/od/objectdetection");
		//cfr/face.jsp -- ${param.image} <%=request.getParameter("image")%>
		return mv;
		
	}
}
