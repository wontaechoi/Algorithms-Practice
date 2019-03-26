def dp(n):
    dp = [1, 3]
    for i in range(2,n):
        dp.append((dp[i-2] *2 + dp[i-1])%10007)
    return dp[n-1]

print(dp(int(input())))