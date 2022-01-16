N = []
for _ in range(7):
   m = int(input())
   if m % 2 :
       N.append(m)
if len(N) == 0 :
    print(-1)
else :
    print(sum(N))
    print(min(N))

    