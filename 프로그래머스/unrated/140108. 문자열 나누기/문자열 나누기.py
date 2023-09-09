def solution(s):
    first, cnt, ans = 0, 0, 0
    for idx, ss in enumerate(s):
        cnt += 1 if s[first] == ss else -1
        if cnt == 0:
            ans += 1
            first = idx + 1
    return ans + 1 if cnt else ans