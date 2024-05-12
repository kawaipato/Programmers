def solution(s):
    ans = s
    for ss in range(1,len(s)//2+1):
            rep, idx = "", 0
            while idx < len(s):
                temp, n = s[idx:idx + ss], 1
                while temp == s[idx+ss:idx+ss*2]:
                    idx, n = idx+ss, n + 1
                rep, idx = rep + ((str(n) + temp) if n != 1 else temp), idx + ss
            ans = rep if len(rep) < len(ans) else ans
    return len(ans)