package tv;

//java application class(non-web)
//web servlet class
public class TVMain {

	public static void main(String[] args) {
		TVFactory fac = new TVFactory();
		TV tv =	fac.getTV(args[0]);
		tv.powerOn();
		tv.soundUp();
		tv.soundDown();
		tv.powerOff();
		
		tv = fac.getTV(args[1]);
		tv.powerOn();
		tv.soundUp();
		tv.soundDown();
		tv.powerOff();

	}

}
