# 아스키 코드
# ord(문자) : 아스키 코드로 반환
# chr(숫자) : 숫자에 맞는 아스키 코드
N = input()

if N.isnumeric is True:
    print(chr(int(N)))
else :
    print(ord(N))