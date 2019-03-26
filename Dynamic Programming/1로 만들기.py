def dp(n):
    d = [0,0,1,1]
    for i in range(4,n+1):
        if i % 3== 0 and i % 2 ==0:
            d.append(min(min(d[i//3] +1, d[i//2] +1),d[i-1]+1))
        elif i % 3 ==0:
            d.append(min(d[i//3] +1, d[i-1]+1))
        elif i % 2 ==0:
            d.append(min(d[i//2] +1, d[i-1]+1))
        else:
            d.append(d[i-1]+1)
    return d[n]

print(dp(int(input())))
        