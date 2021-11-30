package my;

import java.util.HashMap;

import org.springframework.stereotype.Service;

import edu.spring.naverai.NaverService;

@Service("mapservice")
//스프링부트 ioc, di - 스프링 생성
// @Autowired 주입
public class MapService implements NaverService{
	HashMap<String, String> map = new HashMap<String, String>();
	MapService(){
		map.put("이름이 뭐니?", "클로바야");
		map.put("무슨 일을 하니?", "ai  서비스 관련 일을 해");
		map.put("멋진 일을 하는구나", "고마워");
		map.put("난 훌륭한 개발자가 될거야", "넌 할 수 있어");
		map.put("잘 자", "내꿈 꿔");
	}
	public String test(String key) {
		// key-키보드입력내용 전달하면 map에서 해당 key 의 value 리턴
		// 못찾으면 "답변할 수 없습니다" 리턴
		String value = map.get(key);
		if(value == null) {
			value = "답변할 수 없습니다";
		}
		return value;
	}
}


