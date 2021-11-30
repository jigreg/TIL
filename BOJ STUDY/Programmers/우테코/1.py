#우테코 1번
import collections
def solution(arr):
    arr1 = collections.Counter(arr)
    a1 = arr1[1]
    a2 = arr1[2]
    a3 = arr1[3]
    ans = max(a1,a2,a3)
    answer = [ans-a1,ans-a2,ans-a3]
    return answer