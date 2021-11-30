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
		send();//질문입력이전.웰컴메시지
		
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
	alert($("#inputMessage").val())
	//inputMessage  입력값을 messageWindow  출력
	var inputMessage = $("#inputMessage").val();
	if(inputMessage != ""){
		$("#messageWindow").append("<p style='background-color:yellow; border-radius:5px 5px 5px 5px; margin:10px'>" + inputMessage + "</p>");
	}//if end
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
					   //tts 서비스 호출(텍스트 -- 음성 변환 파일 전달 - 오디오 태그 출력)-ajax
					   //  /chatbotvoice url - 전달 파라미터명 text : bubbles[b].data.description 값 - ajax
					   $.ajax({
						   url:'/chatbotvoice',
						   data: {'text' : bubbles[b].data.description},
						   type: 'get',
						   success:function(mp3file){//서버리턴결과 = 음성파일명
							   $("#voice").attr("src", "/naverimages/" + mp3file);
							   $("#voice").get(0).play();
							   //document.getElementById("voice").play();
						   }
					   });//음성변환요청
					   
					
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
	<audio id="voice" src="" ></audio>
	<button id="record_start">음성질문시작</button>
	<button id="record_stop">음성질문종료</button>	
</div>
<!-- 음성질문처리 -->
    <script>
    	//dom객체
        const record = document.getElementById("record_start")
        const stop = document.getElementById("record_stop")
 
        if (navigator.mediaDevices) {
            console.log('getUserMedia supported.')
            const constraints = { audio: true  }
        
       let chunks = []
       navigator.mediaDevices.getUserMedia(constraints)//녹음기 사용 준비되면
           .then(function(stream) {
               const mediaRecorder = new MediaRecorder(stream)//녹음기객체 
               record.onclick = function() {//음성질문시작 버튼 클릭시에
                   mediaRecorder.start()// 음성 녹음 시작하라
                   console.log(mediaRecorder.state)
                   console.log("recorder started")
                   record.style.background = "red"
                   record.style.color = "black"
               }//record.onclick
               
               stop.onclick = function() {//음성질문종료 버튼 클릭시에
                   mediaRecorder.stop()//녹음 정지시켜라
                   console.log(mediaRecorder.state)
                   console.log("recorder stopped")
                   record.style.background = ""
                   record.style.color = ""
               }//stop.onclick
             
             //녹음 시작시킨 상태가 되면 chunks에 녹음 데이터를 저장하라 
             mediaRecorder.ondataavailable = function(e) {
               chunks.push(e.data)
             }  
			//음성질문종료 가 되면 실행하라
            mediaRecorder.onstop = function(e) {
              console.log("data available after MediaRecorder.stop() called.")
	
			//2 chunks 배열에 녹음 데이터 있다-- blob 데이터 음성 가져온다
			const blob = new Blob(chunks, {'type' : "audio/mp3"});
			//4. 다음 녹음 위해 chunks 비워둔다
			chunks = []
			
			//5. 파일 저장한다
			var now = new Date();
			var year = now.getFullYear();// 2011
			var month = ('0' + (now.getMonth() + 1)  ).slice(-2) ; //10
			var day = ('0' + now.getDate()).slice(-2) ;  // 오른쪽부터 2자리 
			var h = ('0' + now.getHours()).slice(-2) ;  // 오른쪽부터 2자리 
			var m = ('0' + now.getMinutes()).slice(-2) ;  // 오른쪽부터 2자리 
			var s = ('0' + now.getSeconds()).slice(-2) ;  // 오른쪽부터 2자리 
			var dateString = year+""+month+""+day+""+h+""+m+""+s; //20111007시분초
			console.log(dateString);
			var mp3file = "chatbot" + dateString + ".mp3";
			var formData = new FormData();//<form action="/mp3upload" method=post 태그 대신 자바스크립트객체
			formData.append("file", blob, mp3file);//<input type=file name="file" >
			//서버 파일 업로드 = ajax 요청
/*1. ajax로 multipart/form-data 방식으로 보낼 때, processData는 일반적으로 서버에 전달되는 data는 query String 형태로 전달되어 집니다.
data 파라미터로 전달된 데이터는 jQuery 내부적으로 쿼리스트링으로 만들어 보내는데, 파일전송에는 이를 피해야함으로 false로 설정해줍니다.
2. contentType은 default 값이 "application/x-www-form = urlencoded; charset = UTF-8" 이므로, 보내줄 때
			multipart/form-data로 전송해야 하기 때문에 false로 설정해줍니다.
*/
			$.ajax({
				url:'/mp3upload', 
				data : formData,
				type: 'post',
				processData : false,
				contentType : false,
				success:function(server){
					alert(server)//잘 받았습니다
					if(server == "잘 받았습니다."){
						$.ajax({
							url:"/chatbotspeech",
							type:'get',
							data:{"filename":mp3file},
							dataType:'json',
							success:function(server2){
								//alert(server2.text)	
								//챗봇 서버에게 질문 입력
								$("#inputMessage").val(server2.text);
								send();
							}
						});
						
					}
				}
				
			});//ajax
            }//mediaRecorder.onstop
               
           })//then 
           .catch(function(err) {
               console.log('The following error occurred: ' + err)
           })
 	}//17번 if  end
	</script>

</body>
</html>



