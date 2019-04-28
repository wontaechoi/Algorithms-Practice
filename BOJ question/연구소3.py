dx = [-1,0,0,1]
dy = [0,-1,1,0]

def sol(visit):
    global all_com, N, v_n, virus
    for i in range(v_n):
        dfs(i, 1, [i])
    min_t = N*N
    for i in all_com:
        visited = [visit[k][:] for k in range(len(visit))]
        for m in i:
            queue = [virus[m]]
            x,y,t = virus[m]
            while queue!=[]:
                x,y,t = queue.pop(0)
                if visited[x][y]!= -2:
                    visited[x][y] = t
                for j in range(4):
                    new_x = x + dx[j]
                    new_y = y + dy[j]
                    new_t = t + 1
                    if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N and visited[new_x][new_y] != -1 and visited[new_x][new_y] != -2:
                        if visited[new_x][new_y] == 0:
                            visited[new_x][new_y] = new_t
                            queue.append((new_x,new_y, new_t))
                        elif visited[new_x][new_y] == -2:
                            
                        else:
                            if visited[new_x][new_y] > new_t:
                                queue.append((new_x,new_y, new_t))
        t = count_t(visited)
        if t < min_t:
            min_t = t
        print(visited)
        print(min_t)
    if min_t == N*N:
        return -1
    return min_t
        
                            
def count_t(visited):
    global N
    max_t = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                return N*N
            if max_t < visited[i][j]:
                max_t = visited[i][j]
    return max_t

def dfs(k, n, l):
    global v_n, M, all_com
    temp = l[:]
    com = []
    if n == M:
        all_com.append(l)
        return
    else:
        for i in range(k+1, v_n):
            temp.extend([i])
            dfs(i, n+1, temp)
            com.append(temp)
            temp = l[:]

        
N, M = map(int,input().split())
visited = []
virus = []
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 2:
            virus.append((i,j,0))
        row[j] = row[j]*-1
    visited.append(row)
v_n = len(virus)
all_com = []
               

print(sol(visited))
'''2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
'''
