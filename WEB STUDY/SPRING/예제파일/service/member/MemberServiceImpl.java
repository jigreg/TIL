package service.member;

public class MemberServiceImpl implements MemberService{
	MemberDAO dao;
	public void setMemberDAO(MemberDAO dao) {
		this.dao = dao;
	}
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
