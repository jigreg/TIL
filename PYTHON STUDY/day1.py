# 1줄 주석
'''
여러줄 주석
'''

# 정수 실수 문자열 논리값 - 단일 데이터 저장 구조
a = 100
print(a)
print(type(a))

b = 100.9;
print(b)
print(type(b))

c = True #False 
print(c)
print(type(c))

d1 = 'python'
d2 = "과정"
print(type(d1) , '-', type(d2))

e = None
print(e)


#내장 기본 함수 목록 확인
print(dir(__builtins__))


# 연산자
a = 10
b = 3

print("a+b=" , a+b)
print("a-b=" , a-b)
print("a*b=" , a*b)
print("a/b=" , a/b)#실수몫 나누기
print("a%b=" , a%b)
print("a**b=" , a**b)#제곱
print("a//b=" , a//b)#정수몫 나누기
print("3.14-3.04=" , 3.14-3.04)

# 숫자 내장 기본 함수 - hex(10) oct(10) bin(10) round(3.14) 

#텍스트

d1 = 'python'
d2 = "과정"
d3 = 100
d4 = 200
d5 = "300";
d6 = "3.14";
print(d1 + d2) #문자열결합(공백 x)
#print(d1 , d2, sep='') #문자열결합(공백x)
print(d4 + d3) #숫자덧셈
print(d1 + str(d3))#문자열결합
print(d3 + int(d5))#숫자덧셈
print(d3 + float(d6))#숫자덧셈

#print(d1 - 3)
print(d1 * 3)
#print(d1 / 3)

#[]-index연산자 [시작:종료]-slice연산자
print(d1[0])
print(d1[0:3])
print(d1[:3])
print(d1[2:])

d7 = "multicampus";
# d7  변수 문자열 내부 cam 단어 포함 
print('cam' in d7) #True/False
print(d7.find('cam'))#index
print(d7.count('cam'))#횟수

print(len(d7))#문자갯수 
print(d7.upper())
print(d7)
print("101010".isnumeric())#0-9  값 
print("java-sql-html-python".split("-"))#4  값

print("multicampus {} 호에 있습니다".format(507))

print("{0} {1} 호에 있습니다".format("삼성캠퍼스", 507))

'''
#int(문자데이터) float(문자데이터)  str(정수나실수)
print("숫자 1개를 입력하시오 : ")
first  = input()

print("숫자 또 1개를 입력하시오 : ")
second  = input()#키보드입력내장함수. 리턴타입 문자열str

print(first.isnumetic())
print(second.isnumetic())
print(int(first) + int(second)) 
'''


# 리스트 튜플 딕셔너리 - 여러 데이터 저장 구조
# list
list1 = [1, 3.14, '리스트', True, [1,2,3]];
print(list1);
print(list1[2]);
print(list1[1:5]);
print(list1 + list1);
print(list1 *3);
print('리스트' in list1);
print(len(list1))
print(len(list1[4]))
print(list1[4][0])


list1.append("마지막에새로추가");
list1.insert(2, "정해진위치에 새로추가");
list1[3] = "True수정";# 존재하는 index 수정
list1.pop();#마지막 데이터 삭제
list1.remove(1);# 첫번째 1 데이터 삭제
del list1[0]#0번 인덱스 삭제

print(list1);


#
tuple1 = (1,2,3,4,5); #수정 불가.ArrayList
print(tuple1);
print(tuple1[0]);
#오류 tuple1[0] = 100;

t1, t2, t3, t4, t5= tuple1;
print(t1, t2, t3, t4, t5)
t1 = 100
print(type(tuple1));
print(type(t1));     


#{  key:value, ....}
dic1 = {"id":1, "pw":3.14, "title":'리스트', "finish":True  }#Map
print(len(dic1))
print(type(dic1))
print(dic1['id'])

print(dic1.keys());#딕셔너리 key 모아서 list 형태 리턴
print(dic1.values());#딕셔너리 값 모아서 list 형태 리턴
print(dic1.items()); # (key, value) 튜플을 모아서 list 형태 리턴

dic1['pw']=1234
dic1['contents']="리스트내용입니다"# 추가 (리스트 불가능)
#del dic1['pw']  
dic1.pop('pw');

print(dic1);

print(dir(__builtins__))#내장 함수- 모든 데이터타입


list2 = [1,2,3,4,5]#리스트타입 적용 함수
print(dir(list2))

str1 = "멀티" #문자열타입 적용 함수
print(dir(str1))


import keyword
print(keyword.kwlist)


# 6장
# 자바 언어 - .... - 파이썬 언어(들여쓰기)
# 딕셔너리 {},  튜플 ()
# 조건문
# if 10 > 5 :print("크다");print("크다2");
if 10 < 5 :
    print("크다")
    print("크다2")
else  :
    print("else  수행")
print("출력된다")

# score 80 이상이고 100 이하 " 이수 " 출력
# score 60 이상이고 80 미만 " 재시험 " 출력
# score 40 이상이고 60 미만 " 재수강 " 출력
# 나머지 ( 0-40 미만) "재입과" 출력
score = 35

import random
score = random.randint(1,100)#1 <=? <= 100 난수 
score = random.randrange(1,101)#1 <=? <= 100 난수


if score >= 80 and score <= 100:
    print("이수")    
elif score >= 60 :
    print(" 재시험 ");
elif score >= 40 :
    print(" 재수강 " );
else :
    print("재입과");

print(score , "수고하셨습니다.");


num = random.randint(1,1000);
#num 변수 저장값이 홀수 짝수 판단 출력
#num : 홀수이다 / 짝수이다

if num % 2 == 0:
    print(num , " :  짝수이다")
else:
    print(num , " :  홀수이다")

'''
print("짝홀수 판단할 숫자를 입력하세요");
key_num=input();
if key_num.isnumeric() :
   key_num =int(key_num); 
   if num % 2 == 0:
        print(key_num , " :  짝수이다")
   else:
        print(key_num , " :  홀수이다") 
else :
    print(key_num , " 의 타입은 " , type(key_num) , " 입니다")
'''
#switch-case == match-case
    

print(bool(0))#False
print(bool(-1))
print(bool(1.9))
print(bool(32541543))

print(bool(None))#False


# 반복문
loop_num = 10
cnt = 0;
#반복 횟수 지정x
while cnt < loop_num :
    print(cnt);
    print("번째 반복중");
    cnt += 1

# 키보드 입력 : 50보다 크면 작은 숫자를 생각해 보세요 출력
#               50보다 작으면 큰 숫자를 생각해 보세요 출력
#               50 이면 게임 종료합니다. 반복 멈춤
mynum = 50;
'''
while True :
    yournum = int(input());#오류발생시 입려값 정수 아닌지 확인
    if mynum < yournum  :
        print("작은 숫자를 생각해 보세요")
    elif mynum > yournum:
        print("큰 숫자를 생각해 보세요")    
    else :
        print("게임 종료합니다")
        break
'''
# 키보드 입력 : 50보다 크면 작은 숫자를 생각해 보세요 출력
#               50보다 작으면 큰 숫자를 생각해 보세요 출력
#               50 이면 아무 것도 안한다.

'''
while True :
    yournum = int(input());#오류발생시 입려값 정수 아닌지 확인
    if mynum < yournum  :
        print("작은 숫자를 생각해 보세요")
    elif mynum > yournum:
        print("큰 숫자를 생각해 보세요")    
    else :
        continue;
'''


#유한횟수
for i in (1,2,3,4,5,6,7,8,9,10):#튜플 데이터 반복
    print(i); 
    print("번째 반복중");

for i in [1,2,3,4,5,6,7,8,9,10]:#리스트 데이터 반복
    print(i); 
    print("번째 반복중");

for i in {1,2,3,4,5,6,7,8,9,10}:#딕셔너리 데이터 반복
    print(i); 
    print("번째 반복중");

print(list(range(1, 11, 1)))# 1부터 11 이전값까지 1씩 증가값 범위 
print(list(range(1, 11)))# 1부터 11 이전값까지 1씩 증가값 범위
print(list(range(11)))# 0부터 11 이전값까지 1씩 증가값 범위

for i in range(11):
    print(i)


list2 = ["python", "multi", 100, True]
print(list2)
#0 인덱스 = 'python'

for i in list2:
    print(i)#list2 데이터

for i in range( len(list2) ) :
    print(i  ,"  번째 인덱스 = " , list2[i] )# list2 인덱스 데이터 같이 출력


# 딕셔너리
dic2 = {"k1":1 , "k2":2, "k3":3, "k4":4, "k5":5}
print(dic2) 
print(dic2.keys()) # [k1, k2, ... k5] 리스트 
print(dic2.values()) # [1,2,3,4,5] 리스트 
print(dic2.items()) # [(k1, 1), () () () ()] 리스트

print(type(("k1", 1)))


for k, v in dic2.items() :
    # 키 k3  이면 출력 생략
    if k == 'k3' :
        continue;
    print(k , "   키의 값은 " , v , "  이다")


    
# 이동문 - break, continue


#함수 - 여러가지 실행 문장 모음. 1개의 기능 구현

# 이름(매개변수)
#매개변수 없는 함수  정의
def hello_3times() :
    print("hello");
    print("hello");
    print("hello");

# 실행 호출
hello_3times()


#매개변수 1개  함수 정의
def message_3times(message) :
    print(message);
    print(message);
    print(message);

# 실행 호출
message_3times("파이썬")


#매개변수 2개 함수 정의
def message_ntimes(message, n) :
    for i in range(1, n+1, 1) :
        print(message);

# 실행 호출
message_ntimes("자바", 10)
# 오류 message_ntimes("자바", "파이썬")
# 자바스크립트 매개변수 갯수 초과 오류 x
# 파이썬 매개변수 갯수 일치
# 자바 매개변수 갯수, 타입 일치

#기본 매개변수 있는 함수 정의
def message_defaulttimes(message, n=5):
    for i in range(1, n+1, 1):
        print(message);

#실행 호출
message_defaulttimes(message="다섯번");
message_defaulttimes("세번", 3);

#가변(갯수 가변적) 매개변수 있는 함수 정의
def dynamic_message(*message, n=5):
     print(type(message))
     print("=========================")
     for i in range(1, n+1, 1):
         for j in message :
             print(j);
     print("=========================")

    
    
#실행 호출
dynamic_message("파이썬", "자바" , "sql");
dynamic_message("파이썬", "자바");
dynamic_message("파이썬");

print(1)
print(1,2,3)
print('a', True, 3.14, 'b',sep="," )

# 리턴값 없는 함수
def no_return():
    print("리턴값없음")

#호출
r1 = no_return()#None
print(r1)

# 리턴값 있는 함수
def return1():
    print("리턴값있음")
    result = 10 + 10
    

#호출
r1 = return1()#None
print(r1)

    
# 리턴값 있는 함수
def return2():
    print("리턴값있음")
    result = 10 + 10
    return result

#호출
r2 = return2()#20
print(r2)

# 리턴값 있는 함수
def return3():
    print("리턴값있음")
    result = 10 + 10
    return result , "리턴값"

#호출
r3 = return3()#20
print(r3[0], r3[1])
print(type(r3))

first, second = return3()
print(first , second);

# 함수-지역변수-함수 내부 선언, 사용범위. 함수 실행 동안 임시 필요 )

global_var = "전역변수"
def var_test():
    local = 10;
    local = 20;
    print(local);#20

    global global_var
    global_var = "전역변수수정" #전역변수값 수정  선언 
    print(global_var)#전역변수수정
    

    
#함수 호출
var_test()
#오류 print(local)
print(global_var)#전역변수수
    

'''
실습 문제
소수 개념 - 1과 자신의 수로만 나누어지는  2 이상의 자연수
1>함수 정의 
def get_prime(su):
    prime = []
    non_prime = []

2부터 su 사이의 모든 수에 대하여 소수인지를 판단하여
소수이면 prime 리스트에 저장하고  합성수이면 non-prime 리스트에 저장한다.
prime과 non_prime 리스트를 리턴한다.

2> 함수 호출
get_prime(100)
소수리스트 - [....]
합성수리스트 - [.....]

'''



















