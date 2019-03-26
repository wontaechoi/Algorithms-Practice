def dp(x):
    dp = [1,2]
    for i in range(2,x):
        dp.append((dp[i-2] + dp[i-1])%10007)
        
    return dp[x-1]
print(dp(int(input())))