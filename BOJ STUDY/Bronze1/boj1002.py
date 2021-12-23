N = int(input())
# 두워의 접점 구하기
# 두점에서 만날때 두 중점 거리 < 반지름의 합
# 한점에서 만날때 외접, 내접 두정점 거리 = 반지름의 합,반지름의 차이(절댓값)
# 안만날때 두 중점 거리 > 반지름의 합, 두 중점 거리 < 반지름 차이(절댓값)
# 무수히 많을 떄 반지름 거리 같을 떄
for _ in range(N):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dis = ((x2-x1) ** 2 + (y2-y1) **2)
    if dis == 0 and r1 == r2:
        print(-1)
    elif dis == (r1 + r2) ** 2 or dis == (r1 - r2) ** 2:
        print(1)
    elif dis > (r1 + r2) ** 2 or dis < (r1 - r2) ** 2:
        print(0)
    elif dis < (r1 + r2) ** 2:
        print(2)
