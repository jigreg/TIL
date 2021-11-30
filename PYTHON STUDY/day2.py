'''
전역변수
def 이름 (매개변수):
    지역변수
    global 전역변수명
    전역변수 = ????
    return ? , ? , ....
'''

'''
# 자바스크립트와 파이썬 함수를 변수처럼 취급= 함수를 일급객체 취급
# 매개변수로 함수 선언 가능, 중첩함수, 리턴함수

def f1():
    print(" 출력 ")



f1();#사용자호출시점 함수 실행

def call_func(func):
    import time
    time.sleep(3)
    func ();
    
call_func(f1)
'''

'''
#   리턴 1문장
def f2(msg):
     return msg * 3;

print( f2("람다") )

'''

'''
print( (lambda msg : msg * 3) ("람다") )# 람다식 정의, 실행, 출력문


print( (lambda x,y : x+y) (1, 2) )# 람다식 정의, 실행, 출력문

print( (lambda  : "파이썬") () )# 람다식 정의, 실행, 출력문
'''   

#함수 - 여러개의 문장으로 구성 1개 기능 구현 단위. 재사용
# 여러개 함수 모아 단위 = 모듈 = *.py
# *.py 파일 여러개 모은 단위 = 패키지

#파이썬 설치와 같이 설치 모듈  리스트 + 경로 

import sys

print(sys.builtin_module_names)
print(sys.path)
print(sys.version)

# input() --Scanner.next()
# --main 명령행 매개변수 입력

for i in sys.argv:#[0]-실행모둘명  [1~]
    print(i)

import os
print(os.name)
print(os.getcwd())
print(os.listdir())

import time
#time.sleep(3)
sec = time.time()#현재시간 초단위
now = time.localtime(sec)#년....
print(sec , now.tm_year , now.tm_mon , now.tm_mday)


print(round(3.54))# print, round  함수 - import 필요없다

#import 방법1-모듈명
import math #4장 숫자 형태 
print(math.trunc(3.54))


#import 방법2- 특정 함수
from math import trunc  
print(trunc(3.54))

#import 방법3- 모든 함수
from math import *  
print(trunc(3.54))
print(sin(50))

#import 방법4-모듈명 대신 별명
import math as mt 
print(mt.trunc(3.54))


import random as ra
print(ra.randint(1, 100)) # 1<= 난수 <= 100
print(ra.randrange(1, 101))# 1<= 난수 <= 100

ran_list = ["abc", "ABC", "가나다", 123]
print(ra.choice(ran_list));
print(ra.sample(ran_list, 3));


# 필요시 모듈 별도 설치  과정 필요
# spring 기본라이브러리 + ajax, upload, mybatis 라이브러리 추가
#mvnrespository 모아서 관리 - pom.xml 작성-다운로드
# 필요한 라이브러리이름 다운로드 -  pip3
# pip3 install 모듈명--도스

# pip3 install beautifulsoup4
# pip list


import urllib.request as req
from bs4 import BeautifulSoup as bs
'''
# 파이썬 웹서버 접속. 응답 
response =req.urlopen("http://localhost:9001/helloboot")
#print(response)#객체유형이름

soup = bs(response, "html.parser")
contents = soup.prettify(); #소스
#print(contents)#모든응답내용  html  소스

#h1태그 작성 내용 찾아서 분석

#print(soup.find("h1"))
#<h1> 전달받은 모델 : hello boot</h1>


#print(soup.find("h1").string)
# 전달받은 모델 : hello boot
'''

'''
print(soup.findAll("h1"))#리스트

print(soup.select("h1"))

print(soup.find("img")['src'])#최초 1개 img

print(soup.select_one("img")['src'])

print(soup.select_one("input")['type'])

print(soup.select_one("form")['action'])
'''

'''
h1_list = soup.findAll("h1")

for h1 in h1_list:
    print(h1.string)


img_list = soup.findAll("img")

for img in img_list:
    print(img['src'])

response.close()
'''

'''
====================================================================================
#기상청 - 화면 하단 - rss -중기예보-전국
#https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
# 도시이름 출력

weather = req.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
weather_bs = bs(weather, "html.parser")

#city 태그 문자열 출력
location_list = weather_bs.findAll("location");

for location in location_list:
    print("------------------------------------")
    print("도시 :" , location.find("city").string) #각 location태그 포함 첫번째 city 태그 문자열
    print("시간 :" , location.select_one("tmEf").string) #각 location태그 포함 첫번째 tmEf 태그  문자열
    print("날씨상태 :" , location.find("wf").string) #각 location태그 포함 첫번째 wf 태그 문자열
    print("최고기온 :" , location.find("tmx").string) #각 location태그 포함 첫번째 tmEf 태그 문자열
    print("최저기온 :" , location.find("tmn").string) #각 location태그 포함 첫번째 tmEf 태그 문자열
    print("------------------------------------")   
    
print("총 도시 수는 " , len(location_list) ,  " 개입니다")


------------------------------------
도시: 서울
시간: 2021-09-19 00:00
날씨상태: 맑음
최고기온: 27
최저기온: 19
------------------------------------
------------------------------------
도시: 인천
시간: 2021-09-19 00:00
날씨상태: 맑음
최고기온: 26
최저기온: 20
------------------------------------
------------------------------------
도시: 수원
시간: 2021-09-19 00:00
날씨상태: 맑음
최고기온: 27
최저기온: 19
------------------------------------
'''

# 그래프 그리기
# pip3 install matplotlib 도스 
# pip show  matplotlib
# pip list

import matplotlib.pyplot as plt

a = [1,2,3, 4,5]
b = [2,4,6,8,10]
c = []
import random
for i in range(1, 6, 1):
    c.append(random.randint(1,10))

print(c)

#그래프설정-한글
plt.rcParams["font.family"] = "Batang";
plt.rcParams["font.size"] = 20
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["xtick.labelsize"] = 10 #x축 제목 글씨크기
plt.rcParams["axes.labelsize"] = 8   #x축 데이터값 글씨크기

#plt.rcParams["lines.linestyle"] = "-.";

'''test1
plt.plot(a,c)#선그래프 
plt.title("graph")
plt.xlabel("x(a)")
plt.ylabel("y(c)")
plt.savefig("graph2.png")
plt.show()

plt.hist(c)#히스토그램(빈도수 그래프)
plt.show()
'''

'''test2
plt.subplots()
plt.plot(a,b)
plt.plot(b,a)
plt.hist(c)
plt.show()
'''


plt.subplot(2,2,1) #2*2개 그래프 영역 1번째그래프
#plt.plot(a,b, 'r')# 빨강 선그래프
plt.plot(a,b, 'ro')
plt.subplot(2,2,2) #2*2개 그래프 영역 2번째그래프
#plt.plot(b,a, 'b' )# 파랑 선그래프
#plt.plot(b, a, 'o')
plt.plot(b, a, 'b--')#"b-o" 

plt.subplot(2,2,3) #2*2개 그래프 영역 3번째그래프
plt.hist(c)

plt.subplot(2, 2, 4)
plt.plot(a,b);
plt.title("그래프")
plt.xlabel("a리스트")
plt.ylabel("b리스트")
plt.show()


'''
# 컴 설치 글꼴들 (*.ttf 파일들 ) - Batang
import matplotlib.font_manager as fm

font_list = []
for f in fm.fontManager.ttflist:
    font_list.append(f.name)

font_list.sort() #리턴값 없음. font_list 정렬 상태 변경

for fname in font_list :
    print(fname)#정렬상태 
'''

# 필요시 개인 구현 컴퓨터 모듈
# 현재 경로 primetest.py  모듈 - get_prime-xxx  호출
'''
import primetest
a, b = primetest.get_prime(50)
print("소수" , a)
print("합성수" , b)
'''











