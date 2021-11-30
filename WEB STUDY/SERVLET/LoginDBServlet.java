package member;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/logindb")
public class LoginDBServlet extends HttpServlet {
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	//요청	
		request.setCharacterEncoding("utf-8");
		String id = request.getParameter("id");
		String user_password = request.getParameter("password");
		//jdbc (member1:1111 member2:2222)
		Connection con = null;
		String result = "";
		try {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		con = DriverManager.getConnection
		("jdbc:oracle:thin:@127.0.0.1:1521:xe", "hr", "hr");
		System.out.println("연결성공");
		
		String sql = "select * from member where memberid = ?";
		PreparedStatement st = con.prepareStatement(sql);
		st.setString(1, id);
		ResultSet rs = st.executeQuery();
		//memberid - primary key(not null+unique)
		//  존재하면 1개, 미존재하면 0개=rs.next() true / false
		
		if(rs.next()) {
			//rs.getString("memberid");
			int db_password = rs.getInt("password");
			String name = rs.getString("membername");
			String email = rs.getString("email");
			if(db_password == Integer.parseInt(user_password) ) {
result = 
"<html><head><style>body{color:blue}</style></head><body><h1>아이디 = " 
+ id + "<br>회원이름 = " + name + "<br> 이메일 = " + email + "</h1></body></html>";
			}//id 존재, 암호 맞다 
			else {
result = 
"<h1>암호가 다릅니다. 다시 <a href='logindb.html' > 로그인 </a> 하세요.</h1>";
			}//id 존재, 암호 다르다
		}//rs.next() if end
		else {
result = 
"<h1>회원 정보를 찾을 수 없습니다.  <a href='logininsert.html' > 회원 가입 </a> 부터 하세요.</h1>";			
		}//id 미존재

		
		con.close();
		System.out.println("연결해제성공");
		}catch(SQLException e) {/**/}
		catch(ClassNotFoundException e) {/**/}	
		
	//응답
		response.setContentType("text/html;charset=utf-8");
		PrintWriter o = response.getWriter();
		o.println(result);
	}

}

