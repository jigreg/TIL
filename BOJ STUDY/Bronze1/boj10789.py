lis = []
for _ in range(5):
    lis.append(list(str(input())))

ans = ''

for i in range(15):
    for j in range(5):
        if i>=len(lis[j]):
            continue
        else :
            ans += lis[j][i]
print(ans)