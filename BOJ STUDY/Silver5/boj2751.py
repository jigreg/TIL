import sys

n = int(sys.stdin.readline())
num_list = [0] * 1000001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(1000001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)