def solution(n,a,b):
    i=0
    while n >= 2:
        n /= 2
        i += 1
    for j in range(1,i+1):
        if abs(b-a) == 1:
            if max(a,b)%2==0:
                break
        a, b = (a+1)//2, (b+1)//2
    return j