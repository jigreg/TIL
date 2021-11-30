N = int(input())
s = []
for _ in range(N):
    m = int(input())
    s.append(m)
    s.sort()
for i in range(N):
    print(s[i])
