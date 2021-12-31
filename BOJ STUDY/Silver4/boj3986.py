n = int(input())

cnt = 0
for _ in range(n):
    voca = input()
    stack = []
    for i in range(len(voca)):
        if len(stack) == 0 or stack[-1] != voca[i]:
            stack.append(voca[i])
        else :
            stack.pop()
    if len(stack) == 0:
        cnt +=1
print(cnt)