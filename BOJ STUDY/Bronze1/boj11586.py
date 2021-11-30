# 처음 숫자 입력 받기, 문자열 숫자 만큼 입력 리스트에 저장, 1 그대로 2 좌우,3 상하 뒤집기
N = int(input())
mirrors = []
for _ in range(N):
    mirror = input()
    mirrors.append(mirror)
n = int(input())

if n == 1:
    print(*mirrors,sep='\n')
elif n == 2:
    for i in range(len(mirrors)):
        mirrors[i] = mirrors[i][::-1] #좌우 바꾸기
    print(*mirrors,sep='\n')
else :
    print(*mirrors[::-1],sep='\n') #상하 바꾸기

