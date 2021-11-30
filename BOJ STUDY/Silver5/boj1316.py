N = int(input())

cnt = 0
for _ in range(N):
    s = input()
    k = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new = s[i+1:]
            if new.count(s[i]) > 0:
                k +=1
    if k == 0:
        cnt += 1
    
print(cnt)

# 다시 풀어보자