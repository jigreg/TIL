n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

ans = n
for i in a:
    i -= b
    if i > 0 :
        if i % c:
            ans += (i //c) + 1
        else :
            ans += i//c
print(ans)