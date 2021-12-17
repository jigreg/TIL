N = int(input())
candies= [list(input()) for _ in range(N)]
ans = 1
def search():
    global ans 
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if candies[i][j-1] == candies[i][j]:
                cnt +=1
                ans = max(ans,cnt)
            else : 
                cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if candies[i-1][j] == candies[i][j]:
                cnt +=1
                ans = max(ans,cnt)
            else : 
                cnt = 1


for i in range(N):
    for j in range(N):
        if j+1 < N:
            candies[i][j], candies[i][j+1] = candies[i][j+1] , candies[i][j]
            search()
            candies[i][j], candies[i][j+1] = candies[i][j], candies[i][j+1]
        if i + 1 < N :
            candies[i][j], candies[i+1][j] = candies[i+1][j] , candies[i][j]
            search()
            candies[i][j], candies[i+1][j] = candies[i][j], candies[i+1][j]
print(ans)