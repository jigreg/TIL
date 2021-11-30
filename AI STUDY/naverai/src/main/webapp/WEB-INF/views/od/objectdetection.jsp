<%@page import="org.json.JSONArray"%>
<%@page import="org.json.JSONObject"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>



<!-- java script에서 String을 json 변환-->
<script src="/jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){
	//$("#names").text('<%=request.getAttribute("odresult")%>');
	<% 
	String odresult = (String)request.getAttribute("odresult"); 
	String imagefile = request.getParameter("image");
	%>
	var json = JSON.parse('<%=odresult%>');
	$("#names").text(json.predictions[0].detection_names);
	for(var i = 0; i <json.predictions[0].num_detections; i++ ){
		/* //1. String을 실수 변환  2.*100  3.실수를 정수로 변환 4. % 연결 5.출력 */
		$("#conf").append(parseInt(parseFloat(json.predictions[0].detection_scores[i]) * 100) + "% , ");
		//html(태그),text(문자열), append(태그 이전내용 추가) 
	}
	
	//캔버스 이미지 표시
	let canvas = document.getElementById("objectcanvas");
	let context = canvas.getContext("2d");
	let image = new Image();
	image.src="/naverimages/<%=imagefile%>";
	image.onload  = function(){
		context.drawImage(image, 0, 0, image.width, image.height);
		var boxes = json.predictions[0].detection_boxes;
		for(var i = 0; i <json.predictions[0].num_detections; i++ ){
			if(json.predictions[0].detection_scores[i] >= 0.9	){
				var y1 = boxes[i][0] * image.height ; //y1  
				var x1 = boxes[i][1] * image.width ; //x1 	
				var y2 = boxes[i][2] * image.height ; //y2  
				var x2 = boxes[i][3] * image.width ; //x2
				context.strokeStyle="green";
				context.lineWidth=5;
				context.strokeRect(x1, y1, x2-x1, y2-y1);
				//사물이름 출력
				context.fillStyle="black";
				context.font="15px batang";
				context.fillText
				(json.predictions[0].detection_names[i]+":"
				+ parseInt(json.predictions[0].detection_scores[i]*100)+"%" , x1+20, y1+20);
			//여러 사진 중  animal = [cat, dog,...] 	
			}
			
			
		}
	}

	
});//ready end

</script>

<div id="names" style="border:2px solid green"></div>
<div id="conf" style="border:2px solid blue"></div>
<canvas id="objectcanvas" width=400 height=400 style="border:2px solid pink"></canvas>

<%--
<!-- jsp에서  String을 json 변환-->
<%
JSONObject obj = new JSONObject(odresult);
JSONArray predictions = (JSONArray)obj.get("predictions");
JSONObject predict = (JSONObject)predictions.get(0);
out.println(predict.get("detection_names"));
%>
 --%>


</body>
</html>