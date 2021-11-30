N = int(input())
bang = []
garo = 0
sero = 0
for i in range(N):
    bang.append(list(input()))

for i in range(N):
    cnt = 0
    for j in range(N):
        if bang[i][j] == ".":
            cnt +=1
        else:
            cnt = 0

        if cnt ==2 :
            garo +=1

for i in range(N):
    cnt = 0
    for j in range(N):
        if bang[j][i] == ".":
            cnt +=1
        else:
            cnt = 0
            
        if cnt ==2 :
            sero +=1
            
print(garo,sero)