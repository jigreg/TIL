hobbit = []

for _ in range(9):
    hobbit.append(int(input()))
answer = sum(hobbit)
n = 0
m = 0
for i in range(8):
    for j in range(i+1,9):
        if answer -(hobbit[i] +hobbit[j]) == 100:
            n = hobbit[i]
            m = hobbit[j]
hobbit.remove(n)
hobbit.remove(m)
hobbit.sort()
for i in hobbit:
    print(i)