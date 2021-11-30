a = int(input())
b= int(input())

c=b//100
d=(b-(c*100))//10
e=(b-(c*100))%10

print(a*e)
print(a*d)
print(a*c)
print(a*b)