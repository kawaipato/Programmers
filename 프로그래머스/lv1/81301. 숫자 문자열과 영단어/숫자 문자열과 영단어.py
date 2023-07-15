def solution(s):
    h = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,j in enumerate(h):
        s=s.replace(j,str(i))
    return int(s)