from collections import Counter
def solution(X, Y):
    x, y = Counter(X), Counter(Y)
    a = list((x & y).elements())
    zero_count = 0
    for i in a:
        if i == '0':
            zero_count += 1
    if len(a) == 0:
        return "-1"
    elif len(a) == zero_count:
        return "0"
    else:
        return ''.join(sorted(a,reverse=True))
            