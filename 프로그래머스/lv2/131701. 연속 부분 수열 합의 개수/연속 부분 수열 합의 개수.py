def solution(elements):
    n = len(elements)
    elements *= 2
    ss = [sum(elements[i:i+limit]) for limit in range(1,n) for i in range(n)]
    return len(set(ss)) + 1