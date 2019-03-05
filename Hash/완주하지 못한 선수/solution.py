def solution(participant, completion):
    par_hash ={}
    for par in participant:
        if par not in par_hash:
            par_hash[par] = 1
        else:
            par_hash[par] += 1
    com_hash = {}
    for com in completion:
        if com not in com_hash:
            com_hash[com] = 1
        else:
            com_hash[com] += 1
    
    for h in par_hash:
        if h not in com_hash:
            answer = h
        elif h in com_hash and par_hash[h] != com_hash[h]:
            answer = h
    return answer