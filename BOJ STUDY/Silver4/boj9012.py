N = int(input())
for _ in range(N):
    stack = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stack.append(ch)
        else : 
            if stack:
                stack.pop()
            else :
                isVPS = False
                break
    if stack:
        isVPS = False
    print('YES' if isVPS else 'NO')