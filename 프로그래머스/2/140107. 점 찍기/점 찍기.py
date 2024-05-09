def solution(k, d):
    ans = 0
    for y in range(0,d+1,k):
        x = d ** 2 - y ** 2
        ans += x ** 0.5 // k + 1
    return ans