d = int(input())
c = list(map(int,input().split()))

if d in  c:
    print(c.count(d))
else :
    print(0)