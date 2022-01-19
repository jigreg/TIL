import sys
N,M = map(list,sys.stdin.readline().split())
N = list(map(int,N))
M = list(map(int,M))

print(sum(N) * sum(M))

