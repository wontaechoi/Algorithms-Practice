up = ['w', 'w','w','w','w','w','w','w','w']
down =['y','y','y','y','y','y','y','y','y']
front=['r','r','r','r','r','r','r','r','r']
back = ['o','o','o','o','o','o','o','o','o']
left=['g','g','g','g','g','g','g','g','g',]
right=['b','b','b','b','b','b','b','b','b',]

def _left_(d):
    global up, down, front, back, left, right
    temp_up = [up[i] for i in range(len(up)) if i % 3==0]
    temp_front = [front[i] for i in range(len(up)) if i % 3==0]
    temp_down = [down[i] for i in range(len(up)) if i % 3==0]
    temp_back=[]
    for i in range(len(up)):
        if i % 3==2:
            temp_back.insert(0,back[i])
    if d== '+':
        
        for i in range(len(up)):
            if i % 3 ==0:
                up[i] = temp_back[i//3]
                front[i] = temp_up[i//3]
                down[i] = temp_front[i//3]
            elif i% 3==2:
                back[i] = temp_down.pop(-1)
        left = [left[7-1],left[4-1],left[1-1],left[8-1],left[5-1],left[2-1],left[9-1],left[6-1],left[3-1]]
        
    else:
        for i in range(len(up)):
            if i % 3 ==0:
                up[i] = temp_front[i//3]
                front[i] = temp_down[i//3]
                down[i] = temp_back[i//3]
            elif i% 3==2:
                back[i] = temp_up.pop(-1)
        left = [left[3-1],left[6-1],left[9-1],left[2-1],left[5-1],left[8-1],left[1-1],left[4-1],left[7-1]]
    
def _right_(d):
    global up, down, front, back, left, right
    temp_up = [up[i] for i in range(len(up)) if i % 3==2]
    temp_front = [front[i] for i in range(len(up)) if i % 3==2]
    temp_down = [down[i] for i in range(len(up)) if i % 3==2]
    temp_back=[]
    for i in range(len(up)):
        if i % 3==0:
            temp_back.insert(0,back[i])
    if d== '+':
        for i in range(len(up)):
            if i % 3 ==2:
                up[i] = temp_front[i//3]
                front[i] = temp_down[i//3]
                down[i] = temp_back[i//3]
                back[i] = temp_up[i//3]
        right = [right[7-1],right[4-1],right[1-1],right[8-1],right[5-1],right[2-1],right[9-1],right[6-1],right[3-1]]
    else:
        for i in range(len(up)):
            if i % 3 ==2:
                up[i] = temp_back[i//3]
                front[i] = temp_up[i//3]
                down[i] = temp_front[i//3]
                back[i] = temp_down[i//3]    
        right = [right[3-1],right[6-1],right[9-1],right[2-1],right[5-1],right[8-1],right[1-1],right[4-1],right[7-1]]
    
def _up_(d):
    global up, down, front, back, left, right
    temp_left = [left[i] for i in range(len(up)) if i < 3]
    temp_front = [front[i] for i in range(len(up)) if i <3]
    temp_right = [right[i] for i in range(len(up)) if i <3]
    temp_back = [back[i] for i in range(len(up)) if i <3]  
    if d== '+':
        for i in range(len(up)):
            if i < 3:
                left[i] = temp_front[i]
                front[i] = temp_right[i]
                right[i] = temp_back[i]
                back[i] = temp_left[i]
        up = [up[7-1],up[4-1],up[1-1],up[8-1],up[5-1],up[2-1],up[9-1],up[6-1],up[3-1]]
    else:
        for i in range(len(up)):
            if i < 3:
                left[i] = temp_back[i]
                front[i] = temp_left[i]
                right[i] = temp_front[i]
                back[i] = temp_right[i]
        up = [up[3-1],up[6-1],up[9-1],up[2-1],up[5-1],up[8-1],up[1-1],up[4-1],up[7-1]]
def _down_(d):
    global up, down, front, back, left, right
    temp_left = [left[i] for i in range(len(up)) if i > 5]
    temp_front = [front[i] for i in range(len(up)) if i> 5]
    temp_right = [right[i] for i in range(len(up)) if i> 5]
    temp_back = [back[i] for i in range(len(up)) if i> 5]  
    if d== '-':
        for i in range(len(up)):
            if i > 5:
                left[i] = temp_front[i%6]
                front[i] = temp_right[i%6]
                right[i] = temp_back[i%6]
                back[i] = temp_left[i%6]
        
        down = [down[3-1],down[6-1],down[9-1],down[2-1],down[5-1],down[8-1],down[1-1],down[4-1],down[7-1]]
    else:
        for i in range(len(up)):
            if i > 5:
                left[i] = temp_back[i%6]
                front[i] = temp_left[i%6]
                right[i] = temp_front[i%6]
                back[i] = temp_right[i%6]
        down = [down[7-1],down[4-1],down[1-1],down[8-1],down[5-1],down[2-1],down[9-1],down[6-1],down[3-1]]
                
def _front_(d):
    global up, down, front, back, left, right
    temp_up = [up[i] for i in range(len(up)) if i > 5]
    temp_left = [left[i] for i in range(len(up)) if i % 3 ==2]
    temp_right = [right[i] for i in range(len(up)) if i % 3 ==0]
    temp_down = [back[i] for i in range(len(up)) if i< 3] 
    if d=='+':
        up = up[:6]+ temp_left
        down = temp_right + down[3:]
        for i in range(len(up)):
            if i % 3 == 2:
                left[i] = temp_down[i//3]
            elif i % 3 ==0:
                right[i] = temp_up[i//3]
        
        front = [front[7-1],front[4-1],front[1-1],front[8-1],front[5-1],front[2-1],front[9-1],front[6-1],front[3-1]]
    
    elif d=='-':
        up = up[:6]+ temp_right
        down = temp_left + down[3:]
        for i in range(len(up)):
            if i % 3 == 2:
                left[i] = temp_up[i//3]
            elif i % 3 ==0:
                right[i] = temp_down[i//3]        
        front = [front[3-1],front[6-1],front[9-1],front[2-1],front[5-1],front[8-1],front[1-1],front[3-1],front[7-1]]

def _back_(d):
    global up, down, front, back, left, right
    temp_up = [up[i] for i in range(len(up)) if i < 3]
    temp_left = [left[i] for i in range(len(up)) if i % 3 ==0]
    temp_right = [right[i] for i in range(len(up)) if i % 3 ==2]
    temp_down = [back[i] for i in range(len(up)) if i> 5]
    if d=='+':
        down = down[:6]+ temp_left
        up = temp_right + up[3:]
        for i in range(len(up)):
            if i % 3 == 0:
                left[i] = temp_up[i//3]
            elif i % 3 ==2:
                right[i] = temp_down[i//3]
        back = [back[6],back[3],back[0],back[7],back[4],back[1],back[8],back[5],back[2]]
    elif d=='-':
        down = down[:6]+ temp_right
        up = temp_left + up[3:]
        for i in range(len(up)):
            if i % 3 == 0:
                left[i] = temp_down[i//3]
            elif i % 3 ==2:
                right[i] = temp_up[i//3] 
        back = [back[2],back[5],back[8],back[1],back[4],back[7],back[0],back[3],back[6]]


'''
_front_('+')
print(up)
_back_('+')
print(up)'''

_up_('-')
_down_('-')
_left_('+')
_right_('+')
print(up)
'''
_left_('-')
print(up)
_up_('-')
print(up)

_left_('+')
print(up)
_up_('-')
print(up)

_left_('-')
print(up)
_up_('-')
print(up)
_up_('-')
print(up)

_left_('+')
print(up)

_up_('+')
print(up)
_up_('+')
print(up)'''