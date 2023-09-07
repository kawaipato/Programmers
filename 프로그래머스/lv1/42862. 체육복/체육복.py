def solution(n, lost, reserve):
    save = set(lost) & set(reserve)
    l = set(lost) - save
    r = set(reserve) - save
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x-1)
        elif x + 1 in l:
            l.remove(x+1)
    return n - len(l)