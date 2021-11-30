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
<%  String [] imageext = {"jpg", "jfif", "png", "gif"}; 
    String [] filelist = (String[])request.getAttribute("filelist");	
	for(int i = 0; i < filelist.length; i++){
		String onefile = filelist[i];
		String onefileext[] = onefile.split("[.]");
		String ext = onefileext[onefileext.length - 1];//각 파일의 확장자
		for(int j = 0; j < imageext.length;j++){
			if(imageext[j].equals(ext)){
%>
			<a href="/ocr?image=<%=onefile %>"> <%=onefile %> </a>
			<img src="/naverimages/<%=onefile %>" width="100" height=100 >	<br>
		
<%				
			}//if
		}//inner for
	}//outer for
	
%>
</body>
</html>