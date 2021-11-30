<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
table, td{
border : 1px solid blue;
}
</style>
<script src="jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){


});
</script>
</head>
<body>
<h1> 구구단표</h1>
<table>
<% 
	for(int i=1; i <=9; i++){
%>
	<tr>
<% 
	for(int j = 2; j <=9; j ++){
%>
	 <td> <%=j + "*" + i + "=" + j*i %></td>
	<%
	}
	%>
	</tr>
	<%
	}
	%>
</table>
<table>
<% 
	for(int i=1; i <=9; i++){
		out.println("<tr>");
	for(int j = 2; j <=9; j ++){
		out.println("<td>" + j + "*" + i + "=" + j*i + "</td>");
	}	
		out.println("</tr>");
	}
%>
</table>
</body>
</html>