package edu.spring.naverai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

import cfr.NaverFaceController;
import chatbot.NaverChatbotController;
import my.MyController;
import obectdetection.NaverObjectDetectionController;
import ocr.NaverOCRController;
import pose.NaverPoseController;
import stt_csr.NaverSpeechController;
import tts_voice.NaverVoiceController;
import upload.UploadController;

@SpringBootApplication
@ComponentScan(basePackageClasses = NaverObjectDetectionController.class)
@ComponentScan(basePackageClasses = NaverFaceController.class)
@ComponentScan(basePackageClasses = NaverPoseController.class)
@ComponentScan(basePackageClasses = NaverSpeechController.class)
@ComponentScan(basePackageClasses = NaverVoiceController.class)
@ComponentScan(basePackageClasses = MyController.class)
@ComponentScan(basePackageClasses = NaverOCRController.class)
@ComponentScan(basePackageClasses = UploadController.class)
@ComponentScan(basePackageClasses = NaverChatbotController.class)
@ComponentScan
public class NaveraiApplication {

	public static void main(String[] args) {
		SpringApplication.run(NaveraiApplication.class, args);
		System.out.println("네이버ai서비스시작");
	}

}
