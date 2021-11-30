T = int(input())

for i in range(T):
    s = input()
    score = 0
    sum = 0
    for j in s:
        if j == 'O':
            score += 1
        else :
            score = 0
        sum += score
    print(sum)
