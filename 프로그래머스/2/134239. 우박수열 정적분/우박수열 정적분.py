def ubak(k):
    s = []
    while k != 1:
        s.append(k)
        k = k / 2 if k % 2 == 0 else k*3+1
    s.append(k)
    return s
def integral(lst):
    a = []
    for idx, l in enumerate(lst[:-1]):
        y1, y2 = l, lst[idx+1]
        a.append(min(y1,y2) + abs(y1 - y2)/2)
    return a

def solution(k, ranges):
    collatz = ubak(k)
    inte = integral(collatz)
    answer, n = [], len(collatz)
    for r in ranges:
        r1, r2 = r
        r2 = r2 if r2 > 0 else n + r2 - 1
        if r1 > r2:
            answer.append(-1)
            continue
        ss = 0
        for x in range(r1, r2):
            ss += inte[x]
        answer.append(ss)
    return answer