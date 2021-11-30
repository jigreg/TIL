N = int(input())
coord = []
for _ in range(N):
    coords = list(map(int,input().split()))
    coord.append(coords)

coord.sort()
for i in range(N):
    print(*coord[i])