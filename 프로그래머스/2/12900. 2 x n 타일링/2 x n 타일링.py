def solution(n):
    ans = 0
    lst = [1 for k in range(n+1)]
    for t in range(2,n+1):
        lst[t] = (lst[t-1] + lst[t-2]) % 1000000007
        
    return lst[-1]