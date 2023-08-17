def solution(want, number, discount):
    a, wants = 0, []
    for w, n in zip(want,number):
        wants += [w] * n
    wants = sorted(wants)
    for i, d in enumerate(discount[:-len(wants)+1]):
        if d in wants:
            if wants == sorted(discount[i:len(wants)+i]):
                a += 1
    return a