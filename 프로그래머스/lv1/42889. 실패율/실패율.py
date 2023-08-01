from collections import Counter
def solution(N, stages):
    c = Counter(stages)
    ha = []
    n = len(stages)
    for i in range(1,N+1):
        if n > 0:
            cnt = c[i]
            ha.append((i,cnt/n))
        else:
            ha.append((i,0))
        n -= cnt
    ha = sorted(ha, key = lambda x : (-x[1],x[0]))
    return [h[0] for h in ha]