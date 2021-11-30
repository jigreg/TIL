'''
import numpy as np
n, m = map(int,input().split())
hang = []
for _ in range(n*2):
    hang.append(list(map(int,input().split())))

for i in range(len(hang)-n):
    print(*(np.array(hang[i]) + np.array(hang[i+n])))
numpy 행렬 연산 모듈 안됨..
'''
n, m = map(int,input().split())
hang = []
for _ in range(n*2):
    hang.append(list(map(int,input().split())))
arr1=hang[:n]
arr2=hang[n:]
for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
for i in arr1:
    print(*i)