def solution(babbling):
    ans, dic = 0, ['aya','ye','woo','ma']
    lst = []
    for b in babbling:
        for d in dic:
            if d * 2 not in b:
                b = b.replace(d,' ')
        if b.strip() == '':
            ans += 1
    return ans