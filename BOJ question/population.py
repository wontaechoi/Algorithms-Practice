dx = [-1, 0, 1, 0] # N E S W
dy = [0, 1, 0, -1]


def dfs(x, y,  c_list, total):
    global checked
    global world
    global L
    global R
    global opened
    checked[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < len(world) and new_x >=0 and new_y >=0 and new_y < len(world):
            if checked[new_x][new_y] != 1:
                if L <=abs(world[x][y]-world[new_x][new_y]) <= R:
                    opened= True
                    c_list.append((new_x,new_y))
                    total += world[new_x][new_y]
                    c_list, total = dfs(new_x,new_y,c_list,total)
    return c_list, total
        
def sol(world, L ,R):
    global checked
    for i in range(len(world)):
        for j in range(len(world)):
            if checked[i][j] != 1:
                c_list, total = dfs(i,j,[(i,j)],world[i][j])
                if opened == True:
                    move_pop(c_list,total)
    if opened == False:
        return 0
    return 1
    
def move_pop(c_list, total):
    global world
    new_pop = total//len(c_list)
    for x, y in c_list:
        world[x][y] = new_pop
    

N, L, R = map(int, input().split())
world = []
for i in range(N):
    row = list(map(int,input().split()))
    world.append(row)

'''N,L,R= 4, 1 ,9
world=[[96, 93 ,74, 30],[60, 90 ,65, 96],[5, 27, 17, 98],[10, 41 ,46, 20]]'''
num_move = 0
while True:
    opened = False
    checked =[[0 for i in range(len(world))] for j in range(len(world))]
    move = sol(world,L,R)
    if move == 0:
        break
    num_move += move
    
print(num_move)