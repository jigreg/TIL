import heapq as hq
import sys

input = sys.stdin.readline
min = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m != 0 :
        hq.heappush(min,(abs(m),m))
    else :
        if min:
            print(hq.heappop(min)[1])
        else :
            print(0)