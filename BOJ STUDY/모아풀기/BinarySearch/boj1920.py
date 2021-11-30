N = int(input())
N_num = list(input().split())
N_num.sort()
M = int(input())
M_num = list(input().split())

def binary_search(a,x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else :
            end = mid -1
    return 0

for i in M_num:
    print(binary_search(N_num,i))