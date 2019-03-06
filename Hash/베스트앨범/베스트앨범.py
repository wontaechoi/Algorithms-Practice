from operator import itemgetter
def solution(genres, plays):
    genre_hash = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in genre_hash:
            genre_hash[genres[i]] = []
            genre_hash[genres[i]].append(0)
            genre_hash[genres[i]].append((i, plays[i]))
            genre_hash[genres[i]][0] += plays[i]
        else:
            genre_hash[genres[i]].append((i, plays[i]))
            genre_hash[genres[i]][0] += plays[i]
    l = list(genre_hash.values())
    l.sort(key=itemgetter(0), reverse = True)
    n = 0
    while n != len(genre_hash):
        l[n].pop(0)
        l[n].sort(key=itemgetter(1), reverse=True) 
        for i in range(0, len(l[n])) :
            if (i >= 2) :
                break
            answer.append(l[n][i][0])
        n+=1
    return answer