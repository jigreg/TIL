t = int(input())
s =0
for i in range(t):
    a,b = input().split()
    text = ''
    for j in b:
        text += int(a)*j
    print(text)