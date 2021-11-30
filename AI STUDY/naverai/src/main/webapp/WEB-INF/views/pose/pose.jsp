<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<% 
	String poseresult = (String)request.getAttribute("poseresult"); 
	String image = request.getParameter("image");
%>
<!-- java script에서 String을 json 변환-->
<script src="/jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){
	$("#result").text('<%=poseresult%>');
	var json = JSON.parse('<%=poseresult%>');
	
	
	var posecanvas = document.getElementById("posecanvas");
	var posecontext = posecanvas.getContext("2d");
	posecontext.fillStyle="red";
	posecontext.font = "15px batang";
	
	var image = new Image();
	image.src = "/naverimages/<%=image%>";
	image.onload = function(){
		posecanvas.width = image.width;
		posecanvas.height = image.height;
		posecontext.drawImage(image, 0, 0, image.width, image.height);
		
		var poseinforms=['','', '',''];
		
			
		for(var i=0; i <json.predictions.length; i++){
			var oneperson = json.predictions[i];

			//for(var j = 0; j <json.predictions[i].length; j++ ){//j 정수
			for(var j in oneperson){ 
				var body = oneperson[j];
				var x = body.x * image.width;
				var y = body.y * image.height;
				posecontext.fillText(j+"번", x,y);//0-17(0:코)
				//posecontext.fillText(poseinforms[j] , x,y);
				//
			}
		}
	}//onload 
	
	
	
});//ready end

</script>
<div id="result" style="border:2px solid green"></div>
<canvas id="posecanvas" width=400 height=400 style="border:2px solid pink"></canvas>

</body>
</html>