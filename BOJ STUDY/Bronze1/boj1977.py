m = int(input())
n = int(input())

sum, min = 0, n*n

for i in range(1,n):
    if(m<=i*i and i*i<= n):
        sum += i*i
        if (i*i<=min) :
            min = i*i

if sum == 0:
    print(-1)
else :
    print(sum)
    print(min)