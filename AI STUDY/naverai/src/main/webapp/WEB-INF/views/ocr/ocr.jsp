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
	String ocrresult = (String)request.getAttribute("ocrresult");//json 
	String image = request.getParameter("image");
%>
<!-- java script에서 String을 json 변환-->
<script src="/jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){
	var dom = $("#ocrcanvas")[0] ;//  dom객체 변환
	var ocrcontext = dom.getContext("2d");
	var image = new Image();
	image.src = "/naverimages/<%=image%>";
	image.onload = function(){
		dom.width = image.width;
		dom.height = image.height;
		ocrcontext.drawImage(image, 0, 0, image.width, image.height);
		//선색상 선굵기 지정
		ocrcontext.strokeStyle="green";
		ocrcontext.lineWidth = 3;
		
		var json = JSON.parse('<%=ocrresult%>');
		var fieldslist = json.images[0].fields;//이미지 글씨 공백 분리 단어 여러개
		//alert(fieldslist[i].boundingPoly.vertices.length);
		for(var i in fieldslist){
			//let , const
			var x = fieldslist[i].boundingPoly.vertices[0].x;
			var y = fieldslist[i].boundingPoly.vertices[0].y;
			var width = fieldslist[i].boundingPoly.vertices[1].x - x;
			var height = fieldslist[i].boundingPoly.vertices[3].y - y;	
			
			ocrcontext.strokeRect(x, y,  width, height);
			////////////////////////////////////////////////////////
			if(fieldslist[i].lineBreak == true){
				$("#result2").append(fieldslist[i].inferText + "<br>");
			}
			else{
				$("#result2").append(fieldslist[i].inferText);
			}
			///////////////////////////////////////////////////////
			
		}
	}
	
});//ready end

</script>
<div id="result" style="border:2px solid green">${ocrresult }</div> 
<div id="result2" style="border:2px solid blue"> </div>
<canvas id="ocrcanvas" width=400 height=400 style="border:2px solid pink"></canvas>

</body>
</html>






