def dfs(k, n, l):
    global a_n, M, all_com
    temp = l[:]
    com = []
    if n == M:
        all_com.append(l)
        return
    else:
        for i in range(k+1, a_n):
            temp.extend([i])
            dfs(i, n+1, temp)
            com.append(temp)
            temp = l[:]
            
all_com = []
a_n = 6
M = int(input())
for i in range(a_n):
    dfs(i,1,[i])
l_bound= float(input())
num_a = int(input())
a_dict = {}

for i in range(num_a):
    line = list(input().split(','))
    for c in all_com:
        if M == 1:
            a=c[0]
            if (line[a]) not in a_dict:
                a_dict[(line[a])] = 1
            else:
                a_dict[(line[a])] += 1            
        elif M ==2:
            a1, a2 = c[0], c[1]
            if (line[a1],line[a2]) not in a_dict:
                a_dict[(line[a1],line[a2])] = 1
            else:
                a_dict[(line[a1],line[a2])] += 1
        elif M ==3:
            a1, a2, a3 = c[0], c[1], c[2]
            if (line[a1],line[a2],line[a3]) not in a_dict:
                a_dict[(line[a1],line[a2],line[a3])] = 1
            else:
                a_dict[(line[a1],line[a2],line[a3])] += 1            
        elif M==4:
            a1, a2, a3,a4 = c[0], c[1], c[2], c[3]
            if (line[a1],line[a2],line[a3],line[a4]) not in a_dict:
                a_dict[(line[a1],line[a2],line[a3],line[a4])] = 1
            else:
                a_dict[(line[a1],line[a2],line[a3],line[a4])] += 1             
        elif M==5:
            a1, a2, a3,a4,a5 = c[0], c[1], c[2], c[3],c[4]
            if (line[a1],line[a2],line[a3],line[a4],line[a5]) not in a_dict:
                a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5])] = 1
            else:
                a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5])] += 1             
        elif M==6:
            a1, a2, a3,a4,a5,a6 = c[0], c[1], c[2], c[3],c[4],c[5]
            if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6]) not in a_dict:
                a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6])] = 1
            else:
                a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6])] += 1             
            
for a in a_dict:
    if (a_dict[a]/num_a) >= l_bound:
        s = ''
        for i in range(M):
            s+=a[i]
            if i < (M-1):
                s+=','
        print(s)

