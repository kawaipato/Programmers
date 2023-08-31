def solution(n, m, section):
    paint, ans = section[0] - 1, 0
    for s in section:
        if paint <= s:
            paint = s + m 
            ans += 1
    return ans