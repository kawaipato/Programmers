def solution(brown, yellow):
    a = brown + yellow
    for i in range(a+1,1,-1):
        if a%i==0:
            if (i-2) * ((a/i) - 2) == yellow:
                break
    return [i,a/i]