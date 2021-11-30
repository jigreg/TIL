package member;

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
				new ClassPathXmlApplicationContext("member/member.xml");
		MemberDAO dao = (MemberDAO)factory.getBean("dao");
		
		if(dao.selectMember() == true) {
			System.out.println("정상 로그인 사용자입니다.");
		};
		dao.insertMember();

	}

}
