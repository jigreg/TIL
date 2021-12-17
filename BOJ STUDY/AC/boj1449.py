n,l = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
cnt = 0 
tmp = 0
for i in s :
    if tmp < i :
        cnt +=1
        tmp = i + l - 1

print(cnt)