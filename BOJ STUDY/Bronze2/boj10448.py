import itertools

def threeNum(n):
    return int(n*(n+1)/2)

arr = []
for i in range(1,1001):
    if(threeNum(i) > 1000):
        break
    arr.append(threeNum(i))
N = int(input())
n = []
for _ in range(N):
    n.append(int(input()))

res = 0
for x in n:
    for i in itertools.product(arr,repeat=3):
        if(sum(i) == x):
            res = 1
            break
    print(res)
    res = 0