N,K = map(int,input().split())
Coins = [int(input()) for _ in range(N)]

Coins.sort(reverse=True)
cnt = 0
for i in Coins:
    if K == 0 :
        break
    cnt += K//i
    K %= i

print(cnt)