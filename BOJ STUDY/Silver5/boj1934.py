# 유클리드 호제법을 활용한 최대공약수, 최소공배수 구하기
N = int(input())
def lcm(a,b):
    return a * b // gcd(a,b)

def gcd(a,b):
    while(b):
        a,b = b,a%b
    return a

for _ in range(N):
    x,y = map(int,input().split())
    print(lcm(x,y))