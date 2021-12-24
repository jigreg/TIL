import heapq as hq,sys

input = sys.stdin.readline
min_heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(min_heap,(abs(x),x))
    else :
        if min_heap :
            print(hq.heappop(min_heap)[1])
        else :
            print(0)
