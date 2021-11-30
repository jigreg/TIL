n = int(input())

#피보나치 F(n) = F(n-1) + F(n-2) n >=2


def fib(n):
    cur ,next = 0,1
    for _ in range(n):
        cur,next = next, cur + next
    return cur

print(fib(n))