dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring(tree_list, ground):
    new_tree_list = []
    dead_tree_list = []
    for i in range(len(tree_list)):
        tree_x = tree_list[i][0]
        tree_y = tree_list[i][1]
        tree_age = tree_list[i][2]
        if tree_age <= ground[tree_x][tree_y]:
            tree_age += 1
            ground[tree_x][tree_y] -= (tree_age -1)
            new_tree_list.append((tree_x, tree_y, tree_age))
        else:
            dead_tree_list.append((tree_x, tree_y, tree_age))
    sorted(new_tree_list, key=lambda tree: tree[2])
    return new_tree_list, dead_tree_list, ground

def summer(dead_tree_list, ground):
    for tree in dead_tree_list:
        tree_x = tree[0]
        tree_y = tree[1]
        tree_age = tree[2]
        ground[tree_x][tree_y] += (tree_age//2)
    return ground

def fall(tree_list):
    for i in range(len(tree_list)):
        tree_x = tree_list[i][0]
        tree_y = tree_list[i][1]
        tree_age = tree_list[i][2] 
        if tree_age % 5 ==0:
            for n in range(8):
                new_x = tree_x + dx[n]
                new_y = tree_y + dy[n]
                if new_x < len(tree_list) and new_x >=0 and new_y >=0 and new_y < len(tree_list):
                    tree_list.append((new_x,new_y,1))
    sorted(tree_list, key=lambda tree: tree[2])
    return tree_list

def winter(ground, nutrient):
    for i in range(len(ground)):
        for j in range(len(ground)):
            ground[i][j] += nutrient[i][j]
    return ground
            
    
def solution(tree_list, ground, nutrient, K):
    for year in range(K):
        new_tree_list, dead_tree_list, ground = spring(tree_list, ground)
        ground = summer(dead_tree_list, ground)
        tree_list = fall(new_tree_list)
        
        ground = winter(ground, nutrient)
    return len(tree_list)

if __name__ == "__main__":
    N,M,K = map(int, input().split())
    ground = [[5 for i in range(N)] for j in range(N)]
    nutrient = []
    for i in range(N):
        row = list(map(int, input().split()))
        nutrient.append(row)
    
    tree_list = []
    for i in range(M):
        x, y, z = map(int, input().split())
        tree_list.append((x-1,y-1,z))
    
    
    sorted(tree_list, key =lambda tree: tree[2])
    
    print(solution(tree_list, ground, nutrient, K))