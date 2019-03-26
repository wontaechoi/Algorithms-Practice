def dp(n):
    d = [0, 1,1,2]
    for i in range(4,n+1):
        d.append(d[i-1]+d[i-2])
    return d[n]

print(dp(int(input())))