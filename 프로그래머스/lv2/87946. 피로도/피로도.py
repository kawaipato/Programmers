from itertools import permutations as p
def solution(k, dungeons):
    m = 0
    l = len(dungeons)
    for j in p(range(l)):
        imsi = k
        for n, i in enumerate(j):
            if imsi < dungeons[i][0]:
                m = max(m,n)
                break
            imsi -= dungeons[i][1]
        else:
            return l
    return m
            