<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
<h1>총 버퍼 크기=<%=out.getBufferSize() %></h1>
<% out.println("출력합니다"); %>
<%="출력합니다2" %>
<%-- 1> 클라이언트 즉각 출력 x
	 2> 서버 jsp 출력 내용 모아서 버퍼 임시 저장 
	 3> 파일 끝 수행 - 브라우저 출력 --%>
<h1>남아있는 버퍼크기=<%=out.getRemaining() %> </h1>
<% out.clearBuffer(); %>

<% Cookie c = new Cookie("book","thisisjava");
   response.addCookie(c);%>
</body>
</html>