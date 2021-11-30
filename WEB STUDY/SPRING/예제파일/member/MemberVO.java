package member;

public class MemberVO {
	String memberid;
	int password;
	String membername;
	String email;
	public MemberVO() {}
	
	public MemberVO(String memberid, int password) {
		super();
		this.memberid = memberid;
		this.password = password;
	}

	public MemberVO(String memberid, int password, String membername, String email) {
		this.memberid = memberid;
		this.password = password;
		this.membername = membername;
		this.email = email;
	}
	public String getMemberid() {
		return memberid;
	}
	public void setMemberid(String memberid) {
		this.memberid = memberid;
	}
	public int getPassword() {
		return password;
	}
	public void setPassword(int password) {
		this.password = password;
	}
	public String getMembername() {
		return membername;
	}
	public void setMembername(String membername) {
		this.membername = membername;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@Override
	public String toString() {
		return "회원아이디=" + memberid + "암호 = " + password + "이름 = " + membername
				+ "이메일= " + email;
	}
	
}
