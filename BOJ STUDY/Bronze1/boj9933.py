n = int(input())
password = []
answ = []
for _ in range(n):
    password.append(list(input()))
    for i in password:
        if i == i[::-1]:
            answ.append(i)
            break
        elif i[::-1] in password:
            answ.append(i)
            break
print(len(answ[0]),answ[0][len(answ[0])//2])
