<%@page import="java.math.BigDecimal"%>
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
<%-- <%		System.out.println("시작2");  %>
<H4>${faceresult }</H4>
<H4><%=request.getAttribute("faceresult") %></H4> --%>

<%  
String faceresult = (String)request.getAttribute("faceresult");
JSONObject obj = new JSONObject(faceresult);
JSONObject info = (JSONObject)obj.get("info");
JSONObject size = (JSONObject)info.get("size");
int width = (Integer)size.get("width");
int height = (Integer)size.get("height");

int faceCount = (Integer)info.get("faceCount");

JSONArray faces = (JSONArray)obj.get("faces");
//[{"celebrity":{"value":"송혜교","confidence":0.678065}}]


for(int i = 0; i < faces.length(); i++){		
	JSONObject oneface = (JSONObject)faces.get(i);
	//{"celebrity":{"value":"송혜교","confidence":0.678065}}

	JSONObject celebrity = (JSONObject)oneface.get("celebrity");
	//{"value":"송혜교","confidence":0.678065}
	String value = (String)celebrity.get("value");
	BigDecimal confidence = (BigDecimal)celebrity.get("confidence");
%>
	<%=width  %> , <%=height %> , <%=faceCount %>, <%=value %>, 
	<%=Math.round(confidence.doubleValue() * 100)  %> % 확률로 닮았습니다. <br>

<%
}
%>
<img src='/naverimages/${param.image }' >
</body>
</html>

<!-- {
"info":{"size":{"width":264,"height":200},"faceCount":1}
,
"faces":[{"celebrity":{"value":"송혜교","confidence":0.678065}}]
} -->


