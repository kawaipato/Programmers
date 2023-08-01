import math
def solution(answers):
    s1 = [1,2,3,4,5] * math.ceil(len(answers)/5)
    s2 = [2,1,2,3,2,4,2,5] * math.ceil(len(answers)/5)
    s3 = [3,3,1,1,2,2,4,4,5,5] * math.ceil(len(answers)/5)
    L,L2 = [], []
    for s in [s1,s2,s3]:
        o = [i for a, i in zip(answers,s[:len(answers)]) if a == i]
        L.append(len(o))
    for i in range(3):
        if max(L) == L[i]:
            L2.append(i+1)
    return L2