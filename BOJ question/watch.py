def check(k, visited):
    global cctv
    if k == len(cctv):
        counted = check_blind_spot(visited)
        return counted, visited
    
    else:
        x = cctv[k][0]
        y = cctv[k][1]
        c = cctv[k][2]
        if c == 1:
            count_list=[]
            visited_list=[]
            for i in range(4):
                temp_visited= [i[:] for i in visited]
            
                if i == 0: 
                    visited0 = dfs(x, y, 0, 1, temp_visited)
                    count0 ,visited0 = check(k+1,visited0)
                    count_list.append(count0)
                    visited_list.append(visited0)
                   
                elif i == 1:
                    visited1 = dfs(x,y, -1, 0, temp_visited)
                    count1,visited1 = check(k+1,visited1)
                    count_list.append(count1)
                    visited_list.append(visited1)
                elif i == 2:  
                    visited2 = dfs(x,y, 0, -1, temp_visited)
                    count2, visited2 = check(k+1,visited2)
                    count_list.append(count2)
                    visited_list.append(visited2)
                    
                elif i == 3:    
                    visited3 = dfs(x,y, 1, 0, temp_visited)
                    count3, visited3 = check(k+1,visited3)
                    count_list.append(count3)
                    visited_list.append(visited3)
                    
            min_count = float("inf")
            min_index = -1
            
            for i in range(len(count_list)):
                if min_count > count_list[i]:
                    min_count = count_list[i]
                    min_index = i
            visited = visited_list[i]
                               
        
        elif c== 2:
            for i in range(2):
                temp_visited= [i[:] for i in visited]
                if i == 0 :
                    visited0= dfs(x, y, 0, -1, temp_visited)  
                    visited0 = dfs(x, y, 0, 1, visited0)
                    count0, visited0 = check(k+1,visited0)
                    
                elif i == 1:
                    visited1= dfs(x, y, -1, 0, temp_visited)  
                    visited1= dfs(x, y, 1, 0, visited1)     
                    count1, visited1 = check(k+1,visited1)
                    
            
            if count0 < count1:
                min_count = count0
                visited = visited0
            else:
                min_count = count1
                visited = visited1
        elif c==3:
            count_list=[]
            visited_list=[]            
            for i in range(4):
                temp_visited= [i[:] for i in visited]
                if i == 0: 
                    visited0 = dfs(x, y, -1, 0, temp_visited)  
                    visited0 =dfs(x, y, 0, 1, visited0)
                    count0, visited0 = check(k+1,visited0)
                    count_list.append(count0)
                    visited_list.append(visited0)                    
                elif i == 1:
                    visited1= dfs(x, y, -1, 0, temp_visited)  
                    visited1= dfs(x, y, 0, -1, visited1)
                    count1, visited1 = check(k+1,visited1)
                    count_list.append(count1)
                    visited_list.append(visited1)      
                    
                elif i == 2:  
                    visited2= dfs(x, y, 1, 0, temp_visited)  
                    visited2= dfs(x, y, 0, -1, visited2)
                    count2, visited2 = check(k+1,visited2)
                    count_list.append(count2)
                    visited_list.append(visited2)
                    
                elif i == 3:    
                    visited3 = dfs(x, y, 1, 0, temp_visited)  
                    visited3 = dfs(x, y, 0, 1, visited3) 
                    count3, visited3 = check(k+1,visited3)
                    count_list.append(count3)
                    visited_list.append(visited3)
                    
            min_count = float("inf")
            min_index = -1
            
            for i in range(len(count_list)):
                if min_count > count_list[i]:
                    min_count = count_list[i]
                    min_index = i
            visited = visited_list[i]
            
        elif c==4:
            count_list=[]
            visited_list=[]                
            for i in range(4):
                temp_visited= [i[:] for i in visited]
                if i == 0: 
                    visited0 = dfs(x, y, -1, 0, temp_visited)  
                    visited0 = dfs(x, y, 0, 1, visited0)
                    visited0 = dfs(x, y, 0, -1, visited0)
                    count0, visited0 = check(k+1,visited0)
                    count_list.append(count0)
                    visited_list.append(visited0)                     
                elif i == 1:
                    visited1 =dfs(x, y, -1, 0, temp_visited)  
                    visited1 =dfs(x, y, 0, -1, visited1)
                    visited1 =dfs(x, y, 1, 0, visited1)
                    count1, visited1 = check(k+1,visited1)
                    count_list.append(count0)
                    visited_list.append(visited0)                     
                elif i == 2:  
                    visited2 =dfs(x, y, 1, 0, temp_visited)  
                    visited2 =dfs(x, y, 0, -1, visited2)
                    visited2 =dfs(x, y, 0, 1, visited2)
                    count2, visited2 = check(k+1,visited2)
                    count_list.append(count0)
                    visited_list.append(visited0)                     
                elif i == 3:    
                    visited3 =dfs(x, y, -1, 0, temp_visited)  
                    visited3 =dfs(x, y, 0, 1, visited3) 
                    visited3 =dfs(x, y, 1, 0, visited3)
                    count3, visited3 = check(k+1,visited3)
                    count_list.append(count0)
                    visited_list.append(visited0) 
                    
            min_count = float("inf")
            min_index = -1
            
            for i in range(len(count_list)):
                if min_count > count_list[i]:
                    min_count = count_list[i]
                    min_index = i
            visited = visited_list[i]
                    
                    
        elif c== 5:
            visited = dfs(x, y, 1, 0, visited)
            visited = dfs(x, y, -1, 0, visited)
            visited = dfs(x, y, 0, 1, visited)
            visited = dfs(x, y, 0, -1, visited)
            
            min_count, visited = check(k+1,visited)
        
    return min_count, visited        
    
def dfs(x, y, d_x, d_y, visited):
    global N, M, office
    
    visited[x][y] = 1
    if office[x][y] == 6:
        visited[x][y] = 6
    else:
        new_x = x + d_x
        new_y = y + d_y
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
            return visited
        if visited[new_x][new_y] != 6:
            visited = dfs(new_x, new_y, d_x,d_y, visited)   
    return visited

def check_blind_spot(visited):
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                count += 1
    return count


N,M = map(int, input().split())
office = []
cctv=[]
visited = [[0 for i in range(M)] for j  in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if 1<= row[j]<= 5:
            cctv.append((i,j, row[j]))
        elif row[j] == 6:
            visited[i][j] = 6
        
    office.append(row)


print(check(0, visited)[0])
