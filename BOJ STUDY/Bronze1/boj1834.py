n = int(input())
ans = 0

for i in range(n+1,n**2,n+1):
    ans += i
print(ans)
