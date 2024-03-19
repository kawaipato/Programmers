def solution(sequence, k):
    ans, start, SUM = [], 0, 0
    for idx, s1 in enumerate(sequence):
        SUM += s1
        while SUM > k:
            SUM -= sequence[start]
            start += 1
        if SUM == k:    ans.append([start,idx])
    ans.sort(key = lambda x: (x[1]-x[0],x[0]))
    return ans[0]
            