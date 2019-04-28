dx = [-1, 0,0, 1] # s, n, e, w
dy = [0, -1, 1,  0]
def find_closest(baby_size,  baby_pos, space):
    baby_x = baby_pos[0]
    baby_y = baby_pos[1]
    fish_l = fish_list[1:baby_size]
    queue = [(baby_x, baby_y, 0)]
    visited = [[0 for j in range(len(space))] for i in range(len(space))]
    while queue != []:
        x, y, time = queue.pop(0)
        visited[x][y] = 1
        if space[x][y] > 0 and space[x][y] < baby_size:
            return x, y,  time
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+ dy[i]
            new_t = time + 1
            if new_x >= 0 and new_x < len(space) and  new_y >= 0 and new_y < len(space):
                if visited[new_x][new_y] == 0:
                    if space[new_x][new_y] <= baby_size:
                        queue.append((new_x, new_y, new_t))
    return -1, -1, -1
            

def sol(baby_size, baby_pos, space):
    time = 0
    baby_x = baby_pos[0]
    baby_y = baby_pos[1]    
    size_up = baby_size
    while True:
        #for r in space:
            #print(r)
        s= []
        space[baby_x][baby_y] = 0
        x, y, seeking_time = find_closest(baby_size,  baby_pos, space)
        if seeking_time == -1:
            return time
        space[x][y] = 0
        baby_pos = (x, y)
        size_up -= 1
        if size_up == 0:
            baby_size += 1
            size_up = baby_size
        time += seeking_time
        

size = int(input())
space = []
baby_size = 2
no_fish_found = 1
fish_list = [[] for i in range(7)]
for i in range(size):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 9:
            baby_pos = (i, j)
        elif row[j] != 0:
            fish_list[row[j]].append((i,j))
            no_fish_found = 0
    space.append(row)
if no_fish_found == 1:
    print(0)
print(sol(baby_size, baby_pos,space))