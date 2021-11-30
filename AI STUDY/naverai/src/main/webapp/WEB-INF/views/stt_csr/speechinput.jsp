<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<% 
	String languages[] = {"Kor", "Jpn", "Chn", "Eng"};
	String languagenames[] = {"한국어", "일본어", "중국어", "영어"};
%>

<form action="/speech"  >
	언어 선택 : <br>
	<%for(int i = 0; i < languages.length; i++ ){ %>
		<input type=radio name="lang" value=<%=languages[i] %> > <%=languagenames[i] %><br>
	<%} %>
	
	<select name="image">
	<%	String[] filelist = (String[])request.getAttribute("filelist");
		//mp3만 추출
		for(int i = 0; i < filelist.length;i++){
			String onefile = filelist[i];
			String[] onefile_split = onefile.split("[.]");  // "."-->모든 1글자 가능 의미 내포 표현 
			String fileext = onefile_split[onefile_split.length-1];
			if(fileext.equals("mp3") || fileext.equals("m4a")){
	%>		
				<option value="<%=onefile %>"> <%=onefile %></option>
	<%      }//if end
		}//for end
	%>	
	</select>
	<input type=submit value="텍스트로변환해주세요">
</form> 


</body>
</html>