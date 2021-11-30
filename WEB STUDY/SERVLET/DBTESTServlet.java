package member;

import java.io.IOException;
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

@WebServlet("/DBTESTServlet")
public class DBTESTServlet extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//요청 
		
		//jdbc
		Connection con = null;
		try {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		con = DriverManager.getConnection
		("jdbc:oracle:thin:@127.0.0.1:1521:xe", "hr", "hr");
		System.out.println("연결성공");
		
		String sql = "select * from member where memberid = ?";
		PreparedStatement st = con.prepareStatement(sql);
		
		st.setString(1, "member1");
		ResultSet rs = st.executeQuery();
		
		while(rs.next()) {
			String name = rs.getString("memberid");
			System.out.println(name);
		}

		con.close();
		System.out.println("연결해제성공");
		}catch(SQLException e) {
			/**/
		}catch(ClassNotFoundException e) {
			System.out.println("드라이버 클래스 위치 확인하세요");
		}
		//응답
	}
}



