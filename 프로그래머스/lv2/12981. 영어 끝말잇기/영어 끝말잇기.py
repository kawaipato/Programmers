import math
def solution(n, words):
    i = 0
    while (i < len(words)-1):
        i += 1
        if words[i][0] != words[i-1][-1]:
            c,d=(i+1)%n,math.ceil((i+1)/n)
            if c == 0:
                c = n
            b = [c,d]
            break
        elif words.count(words[i-1])>1:
            dup = [x for x in words if words.count(x) > 1][-2]
            print(dup)
            # i=words.index(dup)
            i = words.index(dup) + words[words.index(dup)+1:].index(dup)
            c,d=(i+2)%n,math.ceil((i+2)/n)
            if c == 0:
                c = n
            b = [c,d]
            break
        else:
            b = [0,0]
    return b