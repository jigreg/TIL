1.
# 4578
# 1 4 99 35 50 1000
# 1999
# 2 11 20 100 200 600
import sys
si = sys.stdin.readline
W = int(si())
weights = [1, 5, 10, 50, 100, 500]
costs = list(map(int, si().split()))
dp = [[0 for _ in range(W + 1)] for __ in range(6)]
# 0번 보석만 사용했을 때를 가정한 초깃값
for i in range(W + 1):
    dp[0][i] = costs[0] * i
def dp_version():
    global W
    # 점화식
    for k in range(1, 6):
        for w in range(1, W + 1):
            dp[k][w] = dp[k - 1][w]
            if w - weights[k] >= 0:
                dp[k][w] = min(dp[k][w], dp[k][w - weights[k]] + costs[k])
    # 정답
    print(dp[5][W])
def greedy_version():
    global W
    jewels = list(zip(weights, costs))
    jewels.sort(key=lambda x: x[1]/x[0])
    ans = 0
    for w, c in jewels:
        cnt = W // w
        W %= w
        ans += cnt * c
    print(ans)
greedy_version()
2.
import sys
si = sys.stdin.readline
N = int(si())
move_type = si().strip()  # clock, clockwise
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북
ans = [[0 for _ in range(N)] for __ in range(N)]
class Snail:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir
        self.num = 1
        ans[x][y] = 1
    def move(self) -> bool:
        # 이동할 수 있으면 이동하고, 흔적 남기고 True return
        # 없으면 False return
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            self.dir  = (self.dir + 1) % 4
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            return False
        self.x, self.y = nx, ny
        self.num += 1
        ans[nx][ny] = self.num
        return True
snails = [Snail(0, 0, 0), Snail(0, N - 1, 1), Snail(N - 1, N - 1, 2), Snail(N - 1, 0, 3)]
# snails = [Snail(0, 0, 0)]
while True:
    flag = False
    for snail in snails:
        flag |= snail.move()
    if not flag:
        break
if move_type == 'clockwise':
    temp = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = ans[j][i]
    ans = temp
for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()
3.
import sys
si = sys.stdin.readline
N = int(si())
move_type = si().strip()  # clock, clockwise
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북
ans = [[0 for _ in range(N)] for __ in range(N)]
class Snail:
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir
        self.num = 1
        ans[x][y] = 1
    def move(self) -> bool:
        # 이동할 수 있으면 이동하고, 흔적 남기고 True return
        # 없으면 False return
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            self.dir  = (self.dir + 1) % 4
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            return False
        self.x, self.y = nx, ny
        self.num += 1
        ans[nx][ny] = self.num
        return True
snails = [Snail(0, 0, 0), Snail(0, N - 1, 1), Snail(N - 1, N - 1, 2), Snail(N - 1, 0, 3)]
# snails = [Snail(0, 0, 0)]
while True:
    flag = False
    for snail in snails:
        flag |= snail.move()
    if not flag:
        break
if move_type == 'clockwise':
    temp = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = ans[j][i]
    ans = temp
for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()
3.
# 2 2 2
# 1 1
# 2 2
# 12
# 51 37 1
# 17 19
import sys
si = sys.stdin.readline
w, h, D = map(int, si().split())
diagonals = [list(map(int, si().split())) for _ in range(D)]
MOD = 10000019
dp = [[0 for _ in range(h + 1)] for __ in range(w + 1)]
dp[0][0] = 1
for i in range(w + 1):
    for j in range(h + 1):
        if i == 0 and j == 0:
            continue
        dp[i][j] = 0
        if i > 0 :
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD
ans = 0
for diag in diagonals:
    # O -> A -> B -> X
    x, y = diag
    cntAB = (dp[x][y - 1] * dp[w - x + 1][h - y]) % MOD
    # O -> B -> A -> X
    x, y = diag
    cntBA = (dp[x - 1][y] * dp[w - x][h - y + 1]) % MOD
    ans += (cntAB + cntBA) % MOD
    ans %= MOD
print(ans)
4.
# 5
# 1 2
# 1 3
# 2 4
# 2 5
# 4
# 3 4
# 1 2
# 2 3
import sys
si = sys.stdin.readline
N = int(si())
con = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, si().split())
    con[x].append(y)
    con[y].append(x)
dp = [0 for _ in range(N + 1)]
dist = [0 for _ in range(N + 1)]
cnt = [0 for _ in range(N + 1)]
def DFS(x, prev):
    dp[x] = 0
    cnt[x] = 1
    dist[x] = 0
    for y in con[x]:
        if y == prev: continue
        DFS(y, x)
        cnt[x] += cnt[y]
        dp[x] += dp[y]
        dist[x] += dist[y] + cnt[y]
    for y in con[x]:
        if y == prev: continue
        # (y 안에서 시작했기에 생기는 거리 기여도) * (끝으로 가능한 경우의 수)
        dp[x] += (dist[y] + cnt[y]) * (cnt[x] - cnt[y])
DFS(1, -1)
print(dp[1] * 2 - N * (N - 1))
