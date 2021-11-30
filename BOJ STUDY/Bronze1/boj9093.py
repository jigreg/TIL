N = int(input())

for _ in range(N):
    ans  = []
    tk = list(map(str,input().split()))
    for i in tk:
        ans.append(i[::-1])
    print(*ans)