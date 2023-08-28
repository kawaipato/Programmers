def solution(s):
    ans = set()
    result = []
    s=s[2:-2].split('},{')
    s.sort(key = lambda x : len(x))
    for i in s:
        ss = set(list(map(int,i.split(','))))
        result = result + list(ss.difference(ans))
        ans = ss
    return result