<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="vo.MemberVO"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){


});
</script>
</head>
<body>
<%-- <%
//request.setCharacterEncoding("utf-8");
String memberid = request.getParameter("memberid");
String password = request.getParameter("password");
String membername = request.getParameter("membername");
String email = request.getParameter("email");

MemberVO vo = new MemberVO();
vo.setMemberid(memberid);
vo.setPassword(Integer.parseInt(password));
vo.setMembername(membername);
vo.setEmail(email);

%>
아이디:<%=vo.getMemberid() %><br>
암호:<%=vo.getPassword() %><br>
이름:<%=vo.getMembername()%><br>
이메일:<%=vo.getEmail() %><br> --%>

<jsp:useBean id="vo" class="vo.MemberVO"  />

<jsp:setProperty property="*" name="vo"/>

<h1> 액션 태그로 읽어옵니다.</h1>
<jsp:getProperty property="memberid" name="vo" />
<jsp:getProperty property="password" name="vo"/>
<jsp:getProperty property="membername" name="vo"/>
<jsp:getProperty property="email" name="vo" />

</body>
</html>