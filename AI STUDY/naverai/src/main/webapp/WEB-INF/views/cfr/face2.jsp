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
	out.println("얼굴 위치는 x  좌표(왼쪽) " + x  + " , y  좌표(아래로) " + y + " 에서 시작하여 "
	+ "가로 " + width + " 세로 " + height + " 크기를 가집니다.");
	
	//성별 , 나이, 감정, 자세 -confidence   제외 
	/*JSONObject gender = (JSONObject)oneface.get("gender");
	String genderString = (String)gender.get("value");
	JSONObject age = (JSONObject)oneface.get("age");
	String ageString = (String)age.get("value");	
	JSONObject emotion = (JSONObject)oneface.get("emotion");
	String emotionString = (String)emotion.get("value");
	JSONObject pose = (JSONObject)oneface.get("pose");
	String poseString = (String)pose.get("value");
	out.println("<h3>성별=" + genderString);
	out.println(" , 나이=" + ageString);
	out.println(" , 감정=" + emotionString);
	out.println(" , 자세=" + poseString + "</h3>");*/
	
	// 4가지 요소 모두 confidence  : 0.5 이상인 것만 출력
	// 총 x명 있습니다
	// 
}//for end
%>
<img src="/naverimages/${param.image }" >
</body>
</html>