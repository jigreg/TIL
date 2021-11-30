package spring.tv;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

//java application class(non-web)
//web servlet class
public class TVMain {

	public static void main(String[] args) {
		ApplicationContext factory =
		new ClassPathXmlApplicationContext("spring/tv/tv.xml");
		
		TV tv =	(TV)factory.getBean("tv");
		
		tv.powerOn();
		tv.soundUp();
		tv.soundDown();
		tv.powerOff();
		
		TV tv2 =	(TV)factory.getBean("tv");
		TV tv3 =	(TV)factory.getBean("tv");
		TV tv4 =	(TV)factory.getBean("tv");

	}

}
