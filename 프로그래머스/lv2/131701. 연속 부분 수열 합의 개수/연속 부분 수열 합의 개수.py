def solution(elements):
    n = len(elements)
    ans = set()
    for i in range(n):
        ss = elements[i]
        ans.add(ss)
        for j in range(i+1,i+n):
            ss += elements[j%n]
            ans.add(ss)
    return len(ans)