package service.member;

public class MemberDAO {
	MemberVO membervo;
	public void setMembervo(MemberVO vo) {
		membervo = vo;
	}
	
	public boolean selectMember() {
		if(membervo.getMemberid().equals("spring")
		&& membervo.getPassword() == 1111) {
			return true;
		}
		return false;
	}
	public void insertMember() {
		System.out.println(membervo.getMemberid() + " 회원님 정상적으로 회원가입되었습니다.");
	}
}
