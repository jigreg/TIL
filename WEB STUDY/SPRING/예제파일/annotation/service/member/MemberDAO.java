package annotation.service.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDAO {
	@Autowired
	@Qualifier("vo2")
	MemberVO membervo;

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
