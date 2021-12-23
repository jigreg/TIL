N = int(input())
Students = []
for _ in range(N):
    w,h = map(int,input().split())
    Students.append((w,h))

for i in Students:
    cnt = 1
    for j in Students:
        if i[0] < j[0] and i[1] < j[1]:
            cnt +=1
    print(cnt,end=" ")