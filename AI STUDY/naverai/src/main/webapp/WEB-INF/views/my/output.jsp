<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h3 id="response">${response}</h3><br>
<audio id="mp3" src="/naverimages/${responsemp3 }" ></audio>
<script>
//setTimeout(함수, 1000)
document.getElementById("mp3").play();
</script>
</body>
</html>