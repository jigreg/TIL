package upload;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
//<context>cpn... base=p..="upload"
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class UploadController {
	@RequestMapping(value="/fileupload", method=RequestMethod.GET)
	public String uploadForm() {
		return "/upload/uploadform";//file1 이름으로 1개 파일 전송
	}
	
	@RequestMapping(value="/fileupload", method=RequestMethod.POST)
	public ModelAndView uploadResult(MultipartFile file1) throws IOException{
		//파일명 추출
		String filename1 = file1.getOriginalFilename();
		//서버 폴더 설정
		String savePath = "C:/Users/student/Desktop/images/";
		//저장
		File serverfile1 = new File(savePath + filename1);
		file1.transferTo(serverfile1);
	
		ModelAndView mv = new ModelAndView();
		mv.addObject("clientfilename", filename1);
		mv.setViewName("/upload/uploadresult");
		return mv;
	}//uploadResult end
	
	@RequestMapping(value="/ajaxfileupload", method=RequestMethod.POST)
	@ResponseBody
	public String ajaxuploadResult(MultipartFile file1) throws IOException{
		//파일명 추출
		String filename1 = file1.getOriginalFilename();
		//서버 폴더 설정
		String savePath = "C:/Users/student/Desktop/images/";
		//저장
		File serverfile1 = new File(savePath + filename1);
		file1.transferTo(serverfile1);
	
		return filename1+" 파일 잘 받았습니다.";

	}//uploadResult end
	
}
