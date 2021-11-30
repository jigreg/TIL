
n,m = map(int,input().split())
castle = []
for _ in range(n):
    castle.append(list(input()))
a,b = 0,0
for i in range(n):
    if "X" not in castle[i]:
        a +=1

for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        b+=1

print(max(a,b))