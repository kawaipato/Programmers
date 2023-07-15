def solution(k, m, score):
    sums=0
    score.sort(reverse=True)
    if (len(score) // m)==0:
        return 0
    else:
        for i in range(len(score)//m):
            sums+=score[(i+1)*m-1]*m
        return sums