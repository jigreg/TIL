n = int(input())

def fib(n):
    cur , next = 0,1
    for _ in range(n):
        cur, next = next, cur + next
    return cur

print(fib(n))