import sys
a,b,c = map(int,sys.stdin.readline().split())
if a==b==c:
    print(a*1000 +10000) 
elif a==b or a==c:
    print(a*100 + 1000)
elif a==b or b==c :
    print(b*100 + 1000)
elif a==c or b==c:
    print(c*100 + 1000)
else:
    if a>b and a>c:
        print(a*100)
    elif b>a and b>c:
        print(b*100)
    elif c>a and c>b:
        print(c*100)