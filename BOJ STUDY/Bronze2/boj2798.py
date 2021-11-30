a,b = map(int,input().split())
t = list(map(int,input().split()))
answer = 0
for i in range(0,a-2) :
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            if t[i] + t[j] + t[k] > b:
                continue
            else :
                answer = max(answer, t[i] + t[j] + t[k])
print(answer)
