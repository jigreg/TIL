package member;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/loginform")
public class LoginformServlet extends HttpServlet {

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//요청
		request.setCharacterEncoding("utf-8");
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String[] con = request.getParameterValues("con");
		//input type=checkbox <select multiple><option>
		//처리
		String result = "";
		if(pw.length() <= 10) {
			result = "암호 입력 조건 만족하셨습니다.";
		} else {
			result = "암호 입력 조건에 맞지 않습니다.";
		}
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<h3>" + id + " 아이디 받았습니다.</h3>");
		out.println("<h3>" + result + "</h3>");
		for(int i= 0; i<con.length; i++) {
		out.println("<h3> 관심분야 = " + con[i] + "</h3>");
		}
		
		Enumeration e = request.getParameterNames();
		while(e.hasMoreElements()) {
			System.out.println(e.nextElement());
		}
	}

}
