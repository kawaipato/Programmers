def solution(s, skip, index):
    ans = []
    for i in s:
        n = index
        while n != 0:
            if i in ['z','Z']:
                i = chr(ord(i) - 25)
            elif i not in ['z','Z']:
                i = chr(ord(i)+1)
            if i not in skip:
                n -= 1
            print(i)
        ans.append(i)
    return ''.join(ans)