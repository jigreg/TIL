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
<% String image = request.getParameter("image"); %>
<script>
window.onload = function(){
	let facecanvas = document.getElementById("facecanvas");
	let facecontext = facecanvas.getContext("2d");
	
	let copycanvas = document.getElementById("copycanvas");
	let copycontext = copycanvas.getContext('2d');
	
	let faceimage = new Image();
	faceimage.src = "/naverimages/<%=image%>";
	faceimage.onload = function(){
		facecontext.drawImage(faceimage, 0, 0, faceimage.width, faceimage.height);
		 <%  
		 String faceresult2 = (String)request.getAttribute("faceresult2");
		 JSONObject obj = new JSONObject(faceresult2);
		 JSONArray faces = (JSONArray)obj.get("faces");
		 for(int i = 0; i < faces.length(); i++){
		 	JSONObject oneface = (JSONObject)faces.get(i);
		 	JSONObject roi = (JSONObject)oneface.get("roi");
		 	int x = (Integer)roi.get("x");
		 	int y = (Integer)roi.get("y");
		 	int width = (Integer)roi.get("width");
		 	int height = (Integer)roi.get("height");
		 	//out.println("얼굴 위치는 x  좌표(왼쪽) " + x  + " , y  좌표(아래로) " + y + " 에서 시작하여 "
		 	//+ "가로 " + width + " 세로 " + height + " 크기를 가집니다.");
		 %>
		 //자바스크립트문장
		 var x = <%=x%>
		 var y = <%=y%>
		 var width = <%=width%>
		 var height = <%=height%>	
		 
		 facecontext.lineWidth = 3;
		 facecontext.strokeStyle="red";
		 facecontext.strokeRect(x, y, width, height);
		 //var(값 , 선언 중복 ) , let(같은 이름 변수 중복 선언 불가), const(값 수정 불가)
		var copyimage = facecontext.getImageData(x, y, width, height);
		copycontext.putImageData(copyimage, x, y);
		 
		 <%
		 }//for end
		 %> 
	}
	
}

</script>

<canvas id="facecanvas" width=500 height=500 style="border:2px solid purple"></canvas>
<canvas id="copycanvas" width=300 height=300 style="border:2px solid pink"></canvas>
</body>
</html>