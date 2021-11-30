package upload;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class UploadController {
	
	@RequestMapping(value = "/fileupload", method=RequestMethod.GET)
	public String uploadForm() {
		return"/upload/uploadform";
	}
	@RequestMapping(value = "/fileupload", method=RequestMethod.POST)
	public String uploadResult(@ModelAttribute("vo") UploadVO vo) throws IOException{
		//전송파일 2개 객체 생성
		MultipartFile multi1 = vo.getFile1();
		MultipartFile multi2 = vo.getFile2();
		//파일명 추출
		String filename1 = multi1.getOriginalFilename();
		String filename2 = multi2.getOriginalFilename();
		
		//서버 c:/kdigital2/upload 폴더에 저장
		String savePath = "c:/kdigital2/upload/";
		
		String ext1 = filename1.substring(filename1.lastIndexOf("."));
		String ext2 = filename1.substring(filename2.lastIndexOf("."));
		
		filename1 = getUuid() + ext1;
		filename2 = getUuid() + ext2;
		
		File file1 = new File(savePath + filename1);
		File file2 = new File(savePath + filename2);
		
		//저장
		multi1.transferTo(file1);
		multi2.transferTo(file2);
		
		//System.out.println(getUuid());
		
		return "/upload/uploadresult";
	}//uploadresult end
	
	public static String getUuid() {
		return UUID.randomUUID().toString().replaceAll("-", "");//.substring(0,10);
	}
}
