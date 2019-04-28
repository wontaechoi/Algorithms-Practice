import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_poi_hand(op):
    if op == 'R':
        return 'P'
    
    elif op == 'P':
        return 'S'
    
    elif op == 'S':
        return 'R'

def rpc(p1, p2):
    if p1 == p2:
        return 'T'
    l = [p1, p2]
    if 'R' in l and 'S' in l:
        return 'R'
    elif 'P' in l and 'S' in l:
        return 'S'
    elif 'R' in l and 'P' in l:
        return 'P'
    
n = int(input())
i = int(input())
hand = input()
hand_list = []
for h in range(len(hand)):
    if h == i:
        if i % 2== 0 and (i+1)< len(hand):
            hand_list.append(find_poi_hand(hand[h]))
        elif i % 2 != 0:
            hand_list.append(find_poi_hand(hand[h-1]))
    hand_list.append(hand[h])
if i == (n-1):
    hand_list.append(find_poi_hand(hand[i-1]))
change = 0
while len(hand_list) != 1:
    index = 0
    winner = []
    while index < len(hand_list):
        p1 = index
        p2 = index +1 
        if p2 == len(hand_list):
            winner.append(hand_list[p1])
            if p1 == i:
                i = len(winner) -1
            break
        if p1 == i:
            h = find_poi_hand(hand_list[p2])
            if h != hand_list[p1]:
                winner.append(h)
                change +=1
            else:
                winner.append(hand_list[p1])
            i = len(winner) -1
        elif p2 == i:
            h = find_poi_hand(hand_list[p1])
            if h != hand_list[p2]:
                winner.append(h)
                change +=1
            else:
                winner.append(hand_list[p2])
            i = len(winner) -1
        else:
            win = rpc(hand_list[p1],hand_list[p2])
            if win != 'T':
                winner.append(win)
        index += 2
        
    hand_list = winner
print(change)