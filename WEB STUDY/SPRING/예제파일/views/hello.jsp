<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<H1>  컨트롤러부터 전달하는 모델 데이터 </H1>
<h3><%=request.getAttribute("insa") %></h3>
<h3>${insa }</h3>
</body>
</html>