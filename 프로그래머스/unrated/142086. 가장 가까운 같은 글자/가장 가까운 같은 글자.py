def solution(s):
    d= []
    for i in range(len(s)):
        if s[:i + 1].count(s[i]) == 1:
            d.append(-1)
        else:
            cnt = 1
            while(s[i - cnt] != s[i]):
                cnt += 1
            d.append(cnt)
    return d