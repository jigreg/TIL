name = list(input())
x = []
for i in range(len(name)):
    if name[i] == "-":
        i+=1
        x.append(name[i])

strX = "".join(x)
print(name[0]+strX)

'''
n= list(input().split('-'))
ans=''
for i in n:
    ans+=i[0]
print(ans)
'''