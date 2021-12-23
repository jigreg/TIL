T = int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    floar = N % H
    roomnum = (N // H) + 1
    if floar == 0 :
        floar = H
        roomnum = N // H
    print(f'{floar*100+roomnum}')
