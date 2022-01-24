# 연결 요소의 개수
# 무방향 그래프 이고 정점의 개수와 간선의 개수가 주어짐, 간선의 양 끝점이 주어짐
# 연결 요소의 개수를 파악하는 문제
# 인접 행렬을 쓸지 인접 리스트를 쓸지 고민
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7) # 파이썬은 재귀함수 리미트 제한 풀어야함
N,M = map(int,input().split())

adj = [[0] * N for _ in range(N)] #인접행렬

for _ in range(M): # 인접행렬에 정점 담기
    u,v = map(lambda x: x-1,map(int,input().split()))
    adj[u][v] = adj[v][u] = 1

chk = [False] * N # 체크 배열 만들기
ans = 0

def dfs(now): # 재귀로 dfs 돌리기
    for next in range(N):
        if adj[now][next] and not chk[next]:
            chk[next] = True
            dfs(next)

for i in range(N):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)

print(ans)




