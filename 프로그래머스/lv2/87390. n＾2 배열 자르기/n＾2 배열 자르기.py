def solution(n, left, right):
    L=[]
    for i in range(left,right+1):
        L.append(max(i//n,i%n)+1)
    return L