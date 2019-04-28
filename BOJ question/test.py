N = int(input())
test = list(map(int, input().split()))
B, C = map(int,input().split())
total = 0
for i in range(N):
    test[i] -= B
    total += 1
    if test[i] > 0:
        if test[i] % C == 0:
            total += ((test[i] // C))
        else:
            total += ((test[i] // C)+1)
        
    
    test[i] = 0
print(total)