import sys
from collections import deque
input = sys.stdin.readline

def bfs(M,N,box) :
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    days = -1

    while tomato:
        days += 1
        for _ in range(len(tomato)):
            x,y = tomato.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0) :
                    box[nx][ny] = box[x][y] + 1
                    r.append([nx,ny])

    for k in box :
        if 0 in k :
            return -1
    return days

M,N = map(int,input().split())
box = []
tomato = deque()
for i in range(N):
    r = list(map(int,input().split()))
    for j in range(M):
        if r[j] == 1:
            tomato.append([i,j])
    box.append(r)

print(bfs(M,N,box))
