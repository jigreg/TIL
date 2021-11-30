<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<!-- id속성 - java script 태그 후속작업  
     name 속성 - jsp servlet spring 전송 파라미터명
-->
 <input id="text" type=text name="text" >
 <input id="ajaxbtn" type=button value="대화">
 <h3 id="response"></h3>
 <audio id="mp3"> </audio>
 
<!-- submit, reset, button - 출력 버튼 모양 동일( 전송, 초기화, 아무기능 없다) -->
<script src="jquery-3.2.1.min.js" ></script>
<script>
$("#ajaxbtn").on('click', function(){
	$.ajax({
		url : "/mytotal2" , 
		data : {"text" : $("#text").val() }, 
		dataType :"json" , 
		type : "get" , 
		success : function(server){
			$("#response").text(server.response);
			$("#mp3").attr('src', "/naverimages/"+server.mp3);
			$("#mp3").attr('controls', "controls");
			$("#response")[0].innerHTML = "종료";
			
		}//success end
	});//ajax end
});//on end


</script>
</body>
</html>