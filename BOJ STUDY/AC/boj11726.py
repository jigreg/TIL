## n = 2 일 때 2 , n = 3 일때 3, n = 4 일때 5, n = 5 일 때  
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[int(input())])

