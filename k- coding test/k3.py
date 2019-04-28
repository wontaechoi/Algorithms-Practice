import math
n = int(input())
m = int(input())
g = []
for i in range(m):
    g.append(float(input()))
m = int(input())
price = []
guest = []
for i in range(m):
    p = float(input())
    if p > 0:
        price.append(p)
        guest.append(g[i])
    

small_list = []
large_list=[]
equal = False
if len(guest) == 1:
    up = price[0]
else:
    for i in range(len(guest)):
        if n == guest[i]:
            equal = True
            break
        elif n > guest[i]:
            small_list.append((guest[i], price[i]))
        else:
            large_list.append((guest[i], price[i]))

    if equal == True:
        up = price[i]
    else:
        if len(small_list) !=0 and len(large_list)!=0:
            g1, p1= small_list[-1]
            g2, p2 = large_list[0]
        elif len(small_list) == 0:
            g1, p1 = large_list[0]
            g2, p2 = large_list[1]
        elif len(large_list) == 0:
            g1, p1 = small_list[len(small_list)-2]
            g2, p2 = small_list[len(small_list)-1]
            
        delta_g = g2- g1
        delta_p = p2 - p1
        up = p2 - ((g2- n) / delta_g) * delta_p  
            
up = math.floor(up*100.0 + 0.5) /100.0
print(up)