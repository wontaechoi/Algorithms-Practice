def dp(n):
    d = []
    for k in range(n+1):
        d.append([0 for i in range(10)])
    d[1] = [0,1,1,1,1,1,1,1,1,1]
    for i in range(2, n+1):
        for j in range(0,10):
            if j == 0:
                d[i][j] = d[i-1][1]
            elif j== 9:
                d[i][j] = d[i-1][8]
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    return sum([i for i in d[n]])

print(dp(int(input())))