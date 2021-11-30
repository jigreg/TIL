s = []
for i in range(10):
    a = int(input())
    s.append(a%42)
    t = set(s)
print(len(t))