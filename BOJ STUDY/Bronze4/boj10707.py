a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if e-c>0:
    if (e-c)*d +b > a*e :
        print(a*e)
    else :
        print ((e-c)*d + b)
elif e-c==0:
    if e*d +b >a*e :
        print(a*e)
    else :
        print(e*d +b)
else :
    if a*e > b:
        print(b)
    else :
        print(a*e)