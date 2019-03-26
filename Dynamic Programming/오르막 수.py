def dp(n):
    d = []
    for k in range(n+1):
        d.append([0 for i in range(10)])
    d[1] = [1,1,1,1,1,1,1,1,1,1]
    for i in range(2, n+1):
        for j in range(0,10):
            for k in range(j,10):
                d[i][j] +=d[i-1][k]
                
    return sum([i for i in d[n]]) % 10007

print(dp(int(input())))