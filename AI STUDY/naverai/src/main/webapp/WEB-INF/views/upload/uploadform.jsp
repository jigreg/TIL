<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>  파일 전송 폼</h1>
	<form action="/fileupload"  method="post" enctype="multipart/form-data">
	업로드파일명 : <input type="file" name="file1"><br>
	<input type=submit value="파일전송">
	</form>
</body>
</html>