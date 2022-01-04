import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, k = map(int,input().split())
food = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r,c = map(int,input().split())
    food[r-1][c-1] = 1

check = [[False for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y) :
    global cnt 
    check[x][y] = True
    if food[x][y] == 1:
        cnt +=1

    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if food[nx][ny] == 1 and not check [nx][ny]:
                dfs(nx,ny)

res = 0
for i in range(n):
    for j in range(m):
        if food[i][j] == 1 and not check[i][j]:
            cnt = 0
            dfs(i,j)
            res = max(res,cnt)

print(res)