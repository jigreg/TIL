x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

x4 = x1 if x2 == x3 else x2 if x1 == x3 else x3
y4 = y1 if y2 == y3 else y2 if y1 == y3 else y3
print(x4,y4)
