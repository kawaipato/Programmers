def solution(n, s):
    a, b = divmod(s,n)
    if a == 0:
        return [-1]
    ans = [a] * n
    for i in range(b):
        ans[i] += 1
    return ans[::-1]