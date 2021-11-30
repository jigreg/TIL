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
	
	if(session.getAttribute("session1") != null){
		out.println("<h3>" + (String)session.getAttribute("session1") + "</h3>");
	}
	if(session.getAttribute("session2") != null){
		out.println("<h3>" + (MemberVO)session.getAttribute("session2") + "</h3>");
	}

%>


</body>
</html>