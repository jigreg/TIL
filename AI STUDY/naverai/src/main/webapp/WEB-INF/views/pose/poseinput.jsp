<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<c:forEach items="${filelist }" var="onefile">
 <a href="/pose?image=${onefile }"> ${onefile } </a>
<img src="/naverimages/${onefile }"  width=100 height=100> <br>
 
 </c:forEach>


</body>
</html>