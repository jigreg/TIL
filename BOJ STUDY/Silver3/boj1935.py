N = int(input())
S = input()
V = [int(input()) for _ in range(N)]
Stack = []
for ch in S :
    if ch.isalpha():
        Stack.append(V[ord(ch)-ord('A')])
    else :
        b = Stack.pop()
        a = Stack.pop()
        if ch == '+':
            Stack.append(a+b)
        elif ch == '-':
            Stack.append(a-b)
        elif ch == '*':
            Stack.append(a*b)
        else : 
            Stack.append(a/b)

print('{:.2f}'.format(Stack.pop()))

