<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<!-- 1. NaverVoiceService.java -  test 메소드 리턴값을 mp3파일명으로 설정한다 
     2. voiceresult - mp3파일명
-->
<audio  id="mp3" src="/naverimages/${voiceresult}" controls="controls" ></audio>
<script>
 var mp3 = document.getElementById("mp3");
 //mp3.src="/naverimages/${voiceresult}";
 mp3.play();
</script>

</body>
</html>