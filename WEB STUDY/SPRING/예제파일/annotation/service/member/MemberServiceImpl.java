package annotation.service.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service("service")
public class MemberServiceImpl implements MemberService{
	@Autowired
	MemberDAO dao;

	@Override
	public void register() {
		boolean result = dao.selectMember();
		if(!result) {
			dao.insertMember();
		}
		
	}

	@Override
	public void login() {
		boolean result = dao.selectMember();
		if(result) {
			System.out.println("정상적인 로그인 사용자");
		}
		
	}
	
}
