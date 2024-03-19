def solution(sequence, k):
    ans, SUM, now = [], 0, len(sequence) - 1
    for idx, s in enumerate(sequence[::-1]):
        SUM += s
        if SUM < k:
            pass
        elif SUM > k:
            SUM -= sequence[now]
            now -= 1
            if SUM == k:
                ans.append([len(sequence)-1-idx,now])
        else:
            ans.append([len(sequence)-1-idx,now])
    ans.sort(key=lambda x : (x[1]-x[0],x[0]))
    return ans[0]
            
            
            