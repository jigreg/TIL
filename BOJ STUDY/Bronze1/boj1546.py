N = int(input())
M = list(map(int,input().split()))
O = max(M)
score = 0
for i in range(N):
    M[i] = M[i]/O*100
    score += M[i]

print(score/N)