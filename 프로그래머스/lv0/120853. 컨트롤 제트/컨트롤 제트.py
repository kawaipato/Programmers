def solution(s):
    s = s.split()
    Sum = 0
    for i in range(len(s)):
        if s[i] == 'Z':
            Sum -= int(s[i-1])
        else:
            Sum += int(s[i])
    return Sum