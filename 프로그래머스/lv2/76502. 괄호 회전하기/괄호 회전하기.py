def solution(s):
    cnt = 0
    for i in range(len(s)):
        a = s[i:] + s[:i]
        while True:
            a_len = len(a)
            a = a.replace('[]','')
            a = a.replace('{}','')
            a = a.replace('()','')
            if len(a) == 0:
                cnt += 1
                break
            elif a_len == len(a):
                break
    return cnt