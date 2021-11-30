package edu.spring.naverai;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration //현재클래스가 설정 모든 결과를   xml 파일 설정으로 
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/naverimages/**")
        .addResourceLocations("file:///C:/Users/student/Desktop/images/");
    }
}

//  http://localhost:port/upload/파일명
