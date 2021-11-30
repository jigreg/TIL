from itertools import permutations

pool = ['A', 'B', 'C']
print(list(map(''.join, permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, permutations(pool, 2)))) # 2개의 원소로 수열 만들기