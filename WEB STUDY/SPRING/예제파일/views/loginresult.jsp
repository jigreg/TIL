<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>로그인 처리 결과입니다</h1>
<h3>${login } </h3>

<h3><%=request.getAttribute("vo") %></h3>
<h3>${ vo.id } : ${vo.pw }</h3>
<h3></h3>
</body>
</html>