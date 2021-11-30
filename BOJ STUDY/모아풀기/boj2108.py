# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치한 값
# 최빈값 : N개의 수들중 가장 많이 나타나느 낙ㅄ
# 범위 : N개의 수들 중에 최대값과 최솟값차이
import sys
N = int(input())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()
def sanavg (num):
    return round(sum(num) / N)

def center (num):
    return num[N//2]

def frequency (num):
    import collections
    tmp = collections.Counter(num).most_common()
 
    if len(tmp) > 1:
        if tmp[0][1] == tmp[1][1]:
            return tmp[1][0]
        else:
            return tmp[0][0]
    else:
        return tmp[0][0]

def bumwi(num):
    return num[N-1] - num[0]
    

print(sanavg(num))
print(center(num))
print(frequency(num))
print(bumwi(num))
