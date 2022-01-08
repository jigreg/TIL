from collections import deque
n = int(input())
apt = []

for i in range(n):
    apt.append(list(map(int, input())))	

visit = [[0] * n for i in range(n)]		
		
dx = [-1, 0, 1 ,0]						
dy = [0, -1, 0, 1]				

def bfs(x, y, idx):  # bfs 
    q = deque([[x,y]])						
    visit[x][y] = 1				
    while q:
        node = q.popleft()
        for i in range(4):
            nx = node[0] + dx[i]				
            ny = node[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:			
                if apt[nx][ny] == 1 and visit[nx][ny] == 0: 	
                    q.append([nx,ny])				
                    visit[nx][ny] = 1				
                    apt_list[idx] += 1	
                    			
apt_list={}
idx = 0
for i in range(n):						
    for j in range(n):
        if apt[i][j] != 0 and visit[i][j] == 0:			
            apt_list[idx] = 1				
            bfs(i,j,idx)
            idx+=1						
apt_list=sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)