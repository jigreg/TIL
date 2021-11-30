m = int(input())
n = int(input())
prime = []

def is_prime_num(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(m,n+1):
    if is_prime_num(i) == True:
        prime.append(i)


if len(prime) == 0:
    print('-1')
else :
    print(sum(prime))
    print(min(prime))