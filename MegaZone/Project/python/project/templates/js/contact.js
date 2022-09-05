$(document).ready(function(){
    $("#btn1").on("click",function(){      // 클릭 이벤트
      $.ajax({
          url : "http://server.hyejin36.shop:4000",
          dataType: "json",       // 이 부분이 반환 타입을 핸들링하는 곳이다.
          type: "get",
          success: function(data) {
          alert("성공");
          },
          error: function (error){console.log('실패');}
      });
    });
  });
