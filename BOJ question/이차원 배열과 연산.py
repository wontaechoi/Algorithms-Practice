def sol(l, r, c, k):
    r -= 1
    c -= 1
    i = 0
    while True:
        if i > 100:
            return -1
        
        n = len(l)
        m = len(l[0])
        if n>r and m>c and l[r][c] ==k:
            return i
        i+=1
        if n < m:
            l = C(l,n,m)
        else:
            l = R(l,n,m)
    return i

def C(l, n, m):
    new_l = []
    for j in range(m):
        col_dict = [0 for i in range(100)]
        for i in range(n):
            col_dict[l[i][j]] +=1
        col_l=[]
        for k in range(len(col_dict)):
            if col_dict[k] != 0 and k!= 0:
                col_l.append((k, col_dict[k]))
        col_l.sort(key=lambda x: x[1])
        new_col_l = []
        for k in col_l:
            new_col_l.append(k[0])
            new_col_l.append(k[1])
        new_l.append(new_col_l)
    max_len = max_len_R(new_l)
    for k in new_l:
        if len(k) < max_len:
            diff = max_len - len(k)
            for i in range(diff):
                k.append(0)
                
    transpose = [[0 for i in range(len(new_l))] for j in range(len(new_l[0]))]
    for i in range(len(new_l)):
        for j in range(len(new_l[0])):
            transpose[j][i] = new_l[i][j]
    return transpose
        
            
def R(l,n,m):
    new_l = []
    for i in l:
        row_dict = [0 for i in range(100)]
        for j in i:
            row_dict[j] +=1
        row_l=[]
        for k in range(len(row_dict)):
            if row_dict[k] != 0 and k != 0:
                row_l.append((k, row_dict[k]))
        row_l.sort(key= lambda x:x[1])
        new_row_l=[]
        for k in row_l:
            new_row_l.append(k[0])
            new_row_l.append(k[1])
        new_l.append(new_row_l)
    max_len = max_len_R(new_l)
    for k in new_l:
        if len(k) < max_len:
            diff = max_len - len(k)
            for i in range(diff):
                k.append(0)
    return new_l

def max_len_R(l):
    max_len = 0
    for i in l:
        l = len(i)
        if l > max_len:
            max_len = l
    return max_len