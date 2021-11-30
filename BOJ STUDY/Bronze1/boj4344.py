N = int(input())

for i in range(N):
    cnt = 0
    T = list(map(int,input().split()))
    S = T[0]
    del T[0]
    avg = sum(T)/S
    for j in range(S):
        if T[j] > avg:
            cnt += 1


    m = cnt/S*100
    print('{:.3f}%'.format(m))