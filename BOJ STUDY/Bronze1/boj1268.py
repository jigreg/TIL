n = int(input())
cnt = 0
ans=[]
stu=[list(map(int,input().split())) for _ in range(n)]
for i in range(len(stu)):
    for j in range(5):
        if stu[i][j] == stu[i+1][j]:
            cnt+=1
     
print(stu)

#모르겠다...