package service.member;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MemberMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	/*	MemberDAO dao = new MemberDAO();
		MemberVO vo = new MemberVO();
		vo.setMemberid("spring");
		vo.setPassword(1111);

		dao.setMembervo(vo);
		*/
		
		ApplicationContext factory =
				new ClassPathXmlApplicationContext("service/member/member.xml");
		MemberService service = (MemberService)factory.getBean("service");
		
		service.login();
		service.register();
	}

}
