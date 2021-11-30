# bs, matplotlib

# requests - get, post 웹서버 접속 응답
# pip3 install requests

import requests
#  http://localhost:9001/

'''
fromserver = requests.get("http://localhost:9001/hellopython?name=pythontest")
#fromserver = requests.get("http://localhost:9001/helloboot")
print(fromserver.status_code)

if fromserver.status_code == 200 :
    print( fromserver.text )
    print( fromserver.json )#@ResponseBody 선언
    print( fromserver.encoding)
    print ( fromserver.headers['content-type'] )
'''

'''
#<form action="" method=post동일 기능 
fromserver = requests.post("http://localhost:9001/hellopython" , data={'name':'pythontest'})

print(fromserver.status_code)

if fromserver.status_code == 200 :
    print( fromserver.text )
    print( fromserver.json )#@ResponseBody 선언
    print( fromserver.encoding)
    print ( fromserver.headers['content-type'] )
'''
#파이썬 , 그래프 그림 이미지 저장

data_dict={'name':"전송자", "description" : "설명" }

file1 = open('day3.py', 'rt', encoding='utf-8')
file2 = open('D:/backup/k-digital_ 멀티_202107/python교안/city_weather.png', 'rb')
files_dict={'file1': file1, "file2":file2}

fromserver = requests.post("http://localhost:9001/fileupload", data=data_dict  , files=files_dict );
print(fromserver.text)

#파이썬 - > 스프링 서버 -> 마이바티스 - 오라클 db 
# 파이썬 --> oracle 연동 모듈 직접 사용

# 기본 설치 모듈
# 추가 설치 모듈(bs plot requests..)
# 사용자 생성 모듈

import sys
print(sys.path) # 모듈 경로 내부 저장(현재폴더\`, 파이썬\lib  scripts  site-packages

#main.py sub.py
try:
    print(a)
except NameError :
    print("a 선언 확인하세요 ")

try:
    b = [1,2,3]
    print(b[3])
except IndexError as ie:
    print(ie)

try:    
    money = input("대출금액 상환개월수 입력하세요 : ")# 10000 12
    #print(money)
    data = money.split();
    loan = int(data[0])
    payback = int(data[1])
    monthly_return = loan / payback;
    #파이썬 미정의 예외 우리가 정의
    if payback <= 0 :
        raise ValueError("개월수는 음수나 0 은 입력 불가능합니다")
except IndexError :
    print("대출금액이나 상환개월수를 입력하지 않으셨습니다")
except ValueError as ve: #숫자 아니거나 (우리가 정의) 음수
    print(ve)
#except :
#    pass #현재 미구현. 나중에 구현 예정
else :
    #예외없이 정상 시행 실행
    print(loan , ' 금액을 ' , payback , ' 개월로 나누어 상환 예정입니다')
finally : #예외발생여부 무관 항상 실
    print("영업 시간 종료")


# 파일 입출력
'''
텍스트 - 다국어 표현 encoding=utf-8  "t" - xls, csv, txt, json
non-텍스트- 01010101010      "b"   png  gif mp3 mp4 

입력 - "r"
출력 _ "w" "a"

 이미지 파일 입력 - "rb"
  텍스트 출력 - "wt"  "w"

현재 py 모둘 파일과 같은 경로 존재
c:/test/aa/bb/cc/a.py
c:\\test\\aa\\bb\\cc\\a.py
'''

import os
print(os.getcwd())
print(os.listdir())

try:
    file = open("C:/kdigital2/mymodules/main.py", "rt", encoding="utf-8")
    print(file.read())# 파일 통째 입력 
except FileNotFoundError :
    print("파일경로 파일명 확인하세요")
    
file.close();

#  파일 라인 단위 읽어서 1번라인 - xxxxx  리스트 저장

file = open("C:/kdigital2/mymodules/sub.py", "rt", encoding="utf-8")

file_list = []
index = 1
for  line in file: #라인수 반복 \n
    #print(line , end="")
    file_list.append(str(index) + "번라인 - " + line)
    index += 1
file.close()


for line in file_list:
    print(line);

#file = open("D:/backup/k-digital_ 멀티_202107/python교안/weather.png", "rb")
#print(file.read())# python idle 안보인다


#file = open("C:/kdigital2/mymodules/a.txt", "wt")#파일이 없으면 생성
file = open("C:/kdigital2/mymodules/a.txt", "at")#파일이 없으면 생성 . 있으면 기존 내용 추가
file.write('새로운 파일을 생성합니다. \n두번째 줄입니다 \n');
file.close()


# sub.py  파일 입력 - 라인번호 추가 - file_list 저장 - sub_copy.py
file = open("C:/kdigital2/mymodules/sub_copy.py", 'wt', encoding="utf-8")
file.writelines(file_list)
file.close()

# sub.py  파일 입력 - 라인번호 추가 - file_list 저장 내용 가운데 print단어 포함 라인들 - sub_copy_print.py
file = open("C:/kdigital2/mymodules/sub_copy_print.py", 'wt', encoding="utf-8")
for line in file_list :
    #if line.find('print') >= 0:
    if 'print' in line:
        file.write(line)
file.close()




carstate = [] #차량상태만 저장 리스트
carstate_cnt = []
carstate_value = ["폐차직전", "심각한중고","양호한중고", "새차같은중고",  "차량상태"]
file = open("usedcars.csv", "rt")
for line in file:
    line_list = line.split(',')
    mileage = line_list[3]
    if mileage.isdigit() and int(mileage) >= 100000 :
        line_list.append("폐차직전");
    elif mileage.isdigit() and int(mileage) >= 50000 and int(mileage) < 100000:
        line_list.append("심각한중고");
    elif mileage.isdigit() and int(mileage) >= 10000 and int(mileage) < 50000:
        line_list.append("양호한중고")
    elif mileage.isdigit() and int(mileage)  < 10000:
        line_list.append("새차같은중고")
    else: #첫번째줄
        line_list.append("차량상태")
    print(line_list)
    carstate.append(line_list[6])

file.close();


for one_state in carstate_value:
    print( one_state , " : " , carstate.count(one_state))
    carstate_cnt.append(carstate.count(one_state))
    

import matplotlib.pyplot as plt
plt.rcParams['font.family']="Batang"

plt.plot(carstate_value, carstate_cnt)

plt.show()

plt.hist( carstate  )

plt.show()

    
