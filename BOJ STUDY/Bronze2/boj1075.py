'''
두정수 N,F N >=100, F=<100
N=275 f = 5 이면 00 
n = 1021 f =11 이면 01 1001/11 출력 무조건 두자리
'''
N = input()
F = int(input())
n = int(N[:-2] + "00") #문자열 뒤 두자리 없애고 0으로 바꾼것

while True:
    if n % F == 0:
        break
    n +=1
print(str(n)[-2:])