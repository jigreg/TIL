for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n > 1:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

    for j in range(2,n):
        for i in range(2):
            dp[i][j] = max(dp[1-i][j-1], dp[1-i][j-2]) + sticker[i][j]

    print(max(dp[0][n-1], dp[1][n-1]))