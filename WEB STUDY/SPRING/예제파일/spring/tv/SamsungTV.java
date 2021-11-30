package spring.tv;

public class SamsungTV implements TV{
	
	public SamsungTV() {
		System.out.println("삼성TV생성자호출");
	}
	public void powerOn() {
		System.out.println("삼성tv:전원켜다");
	}
	public void powerOff() {
		System.out.println("삼성tv:전원끄다");
	}
	public void soundUp() {
		System.out.println("삼성tv:볼륨높이다");
	}
	public void soundDown() {
		System.out.println("삼성tv:볼륨낮추다");
	}
}
