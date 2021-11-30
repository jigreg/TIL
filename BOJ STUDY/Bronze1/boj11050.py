n,k = map(int,input().split())

# 재귀함수 -- > 트리나 그래프에 유리
def factorial_recursive(t):
    return t * factorial_recursive(t-1) if t > 1 else 1

ans = factorial_recursive(n) / (factorial_recursive(k) * factorial_recursive(n-k))   

print(int(ans))

#import math
#ans = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

'''
def factorial(n) :
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans
'''

'''
def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList
'''

#람다 fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)