a,b,c = map(int,input().split())
d= int(input())

c1=(c+d) %60
b1=(c+d)//60
b2=(b+b1) %60
a1=(b+b1)//60
a2=(a+a1)%24
print(a2,b2,c1)