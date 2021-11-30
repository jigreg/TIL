<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="vo.MemberVO" %>
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
<%
	session.setAttribute("session1", "multicampus");
	session.setAttribute("session2", new MemberVO("member6",6666,"김연결","session@a.com"));
		
	//out.println("서버에 세션 정보를 저장했습니다. ");
%>
<%="서버에 세션 정보를 저장했습니다." %>

</body>
</html>