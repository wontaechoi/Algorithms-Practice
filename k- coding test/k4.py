def dfs(k, n, l):
    global a_n, MM, all_com
    temp = l[:]
    com = []
    if n == MM:
        all_com.append(l)
        return
    else:
        for i in range(k+1, a_n):
            temp.extend([i])
            dfs(i, n+1, temp)
            com.append(temp)
            temp = l[:]
            
all_com = []
a_n = 12
M = int(input())
MM = M -1
a_dict = {}
if M != 12:
    MM = M -1
    for i in range(10):
        dfs(i,1,[i])
    MM = M-2
    for i in range(10):
        dfs(i,1,[i])  
l_bound= float(input())
num_a = int(input())
new_a_c = []
for c in all_com:
    if len(c) == M-1:
        new_a_c.append(c[:M-1].append(11))
        new_a_c.append(c[:M-1].append(12))
    else:
        c.append(11)
        c.append(12)
        new_a_c.append(c)

for i in range(num_a):
    line = list(input().split(','))
    if line[11] == 'capital-loss=None' or line[10] == 'capital-gain=None':
        if M == 12:
                if (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11]) not in a_dict:
                    a_dict[(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11]) ] = 1
                else:
                    a_dict[(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11]) ] += 1
        else:
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
                    elif M ==7:
                        a1, a2, a3,a4,a5,a6,a7 = c[0], c[1], c[2], c[3],c[4],c[5],c[6]
                        if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7]) not in a_dict:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7])] = 1
                        else:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7])] += 1               
                    elif M==8:
                        a1, a2, a3,a4,a5,a6,a7,a8 = c[0], c[1], c[2], c[3],c[4],c[5],c[6],c[7]
                        if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8]) not in a_dict:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8])] = 1
                        else:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8])] += 1             
                    elif M==9:
                        a1, a2, a3,a4,a5,a6,a7,a8,a9 = c[0], c[1], c[2], c[3],c[4],c[5],c[6],c[7],c[8]
                        if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9]) not in a_dict:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9])] = 1
                        else:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9])] += 1             
                    elif M==10:
                        a1, a2, a3,a4,a5,a6,a7,a8,a9,a10 = c[0], c[1], c[2], c[3],c[4],c[5],c[6],c[7],c[8],c[9]
                        if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10]) not in a_dict:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10])] = 1
                        else:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10])] += 1             
                    elif M==11:
                        a1, a2, a3,a4,a5,a6,a7,a8,a9,a10,a11 = c[0], c[1], c[2], c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10]
                        if (line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10],line[a11]) not in a_dict:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10],line[a11])] = 1
                        else:
                            a_dict[(line[a1],line[a2],line[a3],line[a4],line[a5],line[a6],line[a7],line[a8],line[a9],line[a10],line[a11])] += 1             
for a in a_dict:
    if (a_dict[a]/num_a) >= l_bound:
        s = ''
        for i in range(M):
            s+=a[i]
            if i < (M-1):
                s+=','
        print(s)

