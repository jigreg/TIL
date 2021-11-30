package tv;

public class TVFactory {
	public TV getTV(String name) {
		if(name.equals("samsung")) {
			return new SamsungTV();
		}
		else if(name.equals("lg")) {
			return new LgTV();
		} else {
			return null;
		}
	}
}
