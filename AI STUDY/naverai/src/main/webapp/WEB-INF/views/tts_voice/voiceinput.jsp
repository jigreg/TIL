<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<% 
	String speakers[] = {"mijin", "jinho", "clara", "matt", "shinji", "meimei", "liangliang", "jose",
			"carmen", "nnaomi", "nhajun", "ndain"};
	String speakerinforms[] = {"미진 : 한국어, 여성 음색", 
			"진호 : 한국어, 남성 음색", 
			"클라라 : 영어, 여성 음색",
			"매트 : 영어, 남성 음색",
			"신지: 일본어, 남성 음색",
			"메이메이 : 중국어, 여성 음색",
			"량량 : 중국어, 남성 음색",
			"호세 : 스페인어, 남성 음색",
			"카르멘 : 스페인어, 여성 음색",
			"나오미 : 일본어, 여성 음색",
			"하준 : 한국어, 아동 음색 (남)",
			"다인 : 한국어, 아동음색 (여)"};
%>


<form action="/voice"  >
	음색 선택 : <br>
	<%for(int i = 0; i < speakers.length; i++ ){ %>
		<input type=radio name="speaker" value=<%=speakers[i] %> > <%=speakerinforms[i] %><br>
	<%} %>
	
	<select name="text">
	<%	String[] filelist = (String[])request.getAttribute("filelist");
		//txt만 추출
		for(int i = 0; i < filelist.length;i++){
			String onefile = filelist[i];
			String[] onefile_split = onefile.split("[.]");  // "."-->모든 1글자 가능 의미 내포 표현 
			String fileext = onefile_split[onefile_split.length-1];
			if(fileext.equals("txt")){
	%>		
				<option value="<%=onefile %>"> <%=onefile %></option>
	<%      }//if end
		}//for end
	%>	
	</select>
	<input type=submit value="음성으로변환해주세요">
</form> 


</body>
</html>