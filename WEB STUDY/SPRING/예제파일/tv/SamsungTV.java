package tv;

public class SamsungTV implements TV{
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
