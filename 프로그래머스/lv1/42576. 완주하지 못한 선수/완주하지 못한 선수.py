def solution(participant, completion):
    h = {}
    sumh = 0
    for p in participant:
        h[hash(p)] = p
        sumh += hash(p)
    for c in completion:
        sumh -= hash(c)
    
    return h[sumh]