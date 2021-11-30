import sys
N = int(sys.stdin.readline())
members = []
for _ in range(N):
    members.append(list(sys.stdin.readline().split()))

members.sort(key=lambda x:int(x[0]))

for i in members:
    print(*i)