from math import gcd
N = int(input())
def lcm(a,b):
    return a*b // gcd(a,b)
for _ in range(N):
    a,b = map(int,input().split())
    print(lcm(a,b),gcd(a,b))