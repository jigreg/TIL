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
<% application.setAttribute("SHARE", new MemberVO("app",7777,"김사원", "kim@b.net")); %>
<h1><%=application.getAttribute("SHARE")%></h1>
</body>
</html>