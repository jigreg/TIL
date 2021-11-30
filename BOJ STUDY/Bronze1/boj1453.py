N = int(input())
peo = map(int,input().split())
people = list(peo)
people1 = []
for i in people:
    if i not in people1:
        people1.append(i)
if people != people1:
    print(len(people)-len(people1))
else :
    print("0")