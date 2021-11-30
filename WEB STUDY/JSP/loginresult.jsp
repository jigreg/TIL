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
<% 
   if(request.getMethod().equals("POST")){
   request.setCharacterEncoding("utf-8");
   String id = request.getParameter("id");
   String pw = request.getParameter("pw");
   String [] con = request.getParameterValues("con");
//get 방식 한글 전송- 인코딩 설정 별도 필요 X
//post 방식 한글 전송 - 인코딩 설정 별도
%>
<h1> 아이디 = <%=id  %></h1>
<h1> 암호 = <%=pw  %></h1>
<%for(int i = 0; i< con.length; i++){
	%>
<h1> 관심분야 = <%=con[i]  %></h1>
<% 
}
}
%>

<%= request.getMethod() %>
</body>
</html>