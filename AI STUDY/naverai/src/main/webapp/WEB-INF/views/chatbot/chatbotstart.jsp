<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.2.1.min.js"></script>
<script>
$(document).ready(function(){
	$("#enter").on("click", function(){
		//챗팅창 보이게
		$("#chatbox").css("display", "block");
	});
	$("#exit").on("click", function(){
		//챗팅창 안보이게
		$("#chatbox").css("display", "none");
	});
	$("#sendBtn").on("click", function(){
		send();
	});
	$("#inputMessage").on("keyup", function(event){
		if(event.keyCode == 13){
			send();
		}
	});
});//ready end

function send(){
	//inputMessage  입력값을 messageWindow  출력
	var inputMessage = $("#inputMessage").val();
	if(inputMessage != ""){
		$("#messageWindow").append("<p style='background-color:yellow; border-radius:5px 5px 5px 5px; margin:10px'>" + inputMessage + "</p>");
		//챗봇 질문 전달 - 답변 -  ajax요청
		$.ajax({
			url : '/chatbot', 
			type:'post', 
			data : {'message': inputMessage },
			dataType : 'json',
			success : function(response){
				//test1 : 전체 json 출력
				//var string_response = JSON.stringify(response);
				//$("#messageWindow").append
				//("<p style='background-color:white; border-radius:5px 5px 5px 5px; margin:10px'>" + string_response + "</p>");
				
				var bubbles = response.bubbles;
				for(var b in bubbles){
					//test2 : 기본 답변 시작
					if(bubbles[b].type == 'text' ){//텍스트 출력
						$("#messageWindow").append
						("<p style='background-color:white; border-radius:5px 5px 5px 5px; margin:10px'>" 
						+ bubbles[b].data.description + "</p>");
						//기본 답변  url  링크 출력(옵션)
						if(bubbles[b].data.url != null){
							$("#messageWindow").append
							("<a href= " + bubbles[b].data.url + "> " + bubbles[b].data.url + "</a>");
						}
					}// 기본 답변 종료
					//test3 : 이미지 답변/멀티 링크 답변 시작
					else if(bubbles[b].type == 'template'){
						if(bubbles[b].data.cover.type == 'image') { //이미지답변
							$("#messageWindow").append
							("<img src=" + bubbles[b].data.cover.data.imageUrl + " width=200 height=200 >");
						
						}
						else if(bubbles[b].data.cover.type == 'text'){//멀티링크 내부 텍스트답변
							var desc = bubbles[b].data.cover.data.description;
							$("#messageWindow").append
							("<p style='background-color:white; border-radius:5px 5px 5px 5px; margin:10px'>" 
							+ desc + "</p>");
						}
						//이미지 답변/멀티 링크 답변 공통 링크 url - contentTable
						for(var c in bubbles[b].data.contentTable){
							for(var d in bubbles[b].data.contentTable[c]){
								var title = bubbles[b].data.contentTable[c][d].data.title;
								var href = bubbles[b].data.contentTable[c][d].data.data.action.data.url;
								$("#messageWindow").append("<a href=" + href + " > " + title + " </a><br>");
							}
						}
					}//else if 이미지 답변/멀티 링크 답변 종료
					
				}//for end
			
			},
			error : function(e) {alert(e);}, 
			complete : function(){alert(" 종료 ");  $("#inputMessage").val(""); }
		});//ajax end
		
	}
	$("#inputMessage").val("");
}
</script>
</head>
<body>
<button id="enter">입장</button>
<button id="exit">퇴장</button>

<div id="chatbox" style="display:none" >
	<div id="messageWindow" style="background-color:#abcdef; width:500px; height:600px;overflow:scroll;"></div>
	<input id="inputMessage" type=text style="width:400px;">
	<button id="sendBtn">전송</button>
</div>
</body>
</html>