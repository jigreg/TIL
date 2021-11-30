A = int(input())
B = int(input())
C = int(input())
i = 1
Mul = str(A*B*C)
for i in range(10):
    print(Mul.count(str(i)))
    i += i