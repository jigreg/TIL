n,m = input().split()
n = int(n)
m = int(m)

visit = [0]*(n+1)
arr = [0]*(m+1)

def is_not_duplicate(num):
    if visit[num] == 0:
        return True
    else :
        return False

def check(x):
    if x == m+1:
        for i in range(1,m+1):
            print(arr[i],end= ' ')
        print()
    else :
        for i in range(1,n+1):
            if is_not_duplicate(i):
                visit[i] = 1
                arr[x] = i
                check(x+1)
                arr[x] =0
                visit[i] = 0
check(1)