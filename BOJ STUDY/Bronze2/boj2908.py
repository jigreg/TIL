a, b = map(str,input().split())
c ,d= (a[::-1],b[::-1])
if c>d:
    print(c)
else :
    print(d)