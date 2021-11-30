def get_prime(su):
    prime = []
    non_prime = []
    for i in range(2, su+1):
        cnt = 0
        for j in range(1,i):
            if i % j == 0 : cnt += 1
        if cnt == 1 :
            prime.append(i);
        else :
            non_prime.append(i);
    return prime, non_prime

prime_list, non_prime_list = get_prime(100)
print("소수리스트 - ", prime_list)
print("합성수리스트 - ", non_prime_list)
