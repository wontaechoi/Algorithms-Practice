def dp(n):
    dp = [0, 1, 2, 4]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] +dp[i-3])
    return dp[n]

n = int(input())
for i in range(n):
    print(dp(int(input())))
