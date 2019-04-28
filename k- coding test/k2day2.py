import math
def compute_similarity(user, i, rate_diff):
    global num_items, user_rate
    numerator = 0
    denom1 = 0
    denom2 = 0    
    for n in range(num_items):
        if n in user_rate[user] and n in user_rate[i]:
            numerator += rate_diff[user][n] * rate_diff[i][n]
            denom1 += rate_diff[user][n] **2
            denom2 += rate_diff[i][n]**2
    if denom1 == 0 or denom2==0:
        sim = 0
    else:
        sim = numerator/(math.sqrt(denom1)*math.sqrt(denom2))
    return i, sim

def similarity(user, rate_diff):
    global num_users, num_items
    sim_list = []
    for i in range(num_users):
        if i == user:
            continue
        else:
            sim_list.append(compute_similarity(user, i, rate_diff))
    sim_list.sort(key = lambda x: x[1], reverse= True)
    return sim_list


def rate(user, k_sim_user, rate_diff,  user_w_a):
    global num_items, num_sim_user_topk, user_rate, rating_matrix, weighted_average
    new_rate = [0 for i in range(num_items)]
    
    for n in range(num_items):
        summation = 0
        normalize_deno = 0
        for i in range(num_sim_user_topk):
            index, sim = k_sim_user[i]
            
            if n in user_rate[index] and n not in user_rate[user]:
                summation += sim * rate_diff[index][n]
                normalize_deno += abs(sim)
                
        if normalize_deno == 0:
            normalize = 0
        else:
            normalize = 1 / normalize_deno  
        new_rating = user_w_a + normalize * summation
        
        new_rate[n] = (n, new_rating)
    
    new_rate.sort(key = lambda x:x[1], reverse= True)
    return new_rate



num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())

rating_matrix = [[0 for i in range(num_items)] for j in range(num_users)]
user_rate = [[]for i in range(num_users)]
for i in range(num_rows):
    info = input().split()
    userid, itemid, rating = (int)(info[0]), (int)(info[1]), (float)(info[2])
    rating_matrix[userid-1][itemid-1] = rating
    
    user_rate[userid-1].append(itemid-1)

num_reco_users = int(input())
reco_users = []
for i in range(num_reco_users):
    reco_users.append(int(input())-1)


weighted_average = []
for user in range(num_users):
    summation = 0
    for r in rating_matrix[user]:
        summation += r
    weighted_average.append(summation / len(user_rate[user]))
    

rate_diff = [[0 for i in range(num_items)] for j in range(num_users)]

for i in range(num_users):
    for j in range(num_items):
        rate_diff[i][j] = rating_matrix[i][j] - weighted_average[i]

for n in range(num_reco_users):
    k_sim_user = similarity(reco_users[n], rate_diff)[:num_sim_user_topk]
    print(similarity(reco_users[n], rate_diff))
    new_rate = rate(reco_users[n], k_sim_user, rate_diff, weighted_average[reco_users[n]])
    print(new_rate)
    ans = ''
    k = 0
    index = 0
    
    while k < num_item_rec_topk and index< num_items:
        i = new_rate[index][0]
        
        if i not in user_rate[reco_users[n]]:
            
            ans += str(i+ 1)
            if (k+1) != num_item_rec_topk:
                ans+=' '
            k +=1
        index += 1
        
    print(ans)