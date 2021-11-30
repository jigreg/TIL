a,b = map(int,input().split())
c= (a+b)//2
if a-b<0 or (a-b)%2!=0:
    print(-1)
else:
    print(c,(a-c))