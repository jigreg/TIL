<%@ page contentType="text/html; charset=UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<% String idvalue = "아이디 입력"; %>
<h1> 회원 로그인 정보 입력창</h1>
<!-- <form action="http://localhost:9091/servlettest/loginform"> -->
<form action="loginresult.jsp" method='get'>	
	아이디 입력 : <input type = text name= "id" value='<%=idvalue %>'><br>
	암호 입력 : <input type = password name= "pw"   ><br>
	관심 분야 : 
	<input type = 'checkbox' name = "con"  value = "경제 ">	경제 <br>
	<input type = 'checkbox' name = "con"  value = "주식 ">	주식<br>
	<input type = 'checkbox' name = "con"  value = "코딩 ">	코딩 <br>
	<input type = 'checkbox' name = "con"  value = "ai ">	ai<br>
	<input type= submit value="로그인">
</form>
</body>
</html>