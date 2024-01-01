def solution(n, t, m, p):
    ans = "0"
    punto = "0123456789ABCDEF"
    for num in range(1,t*m):
        res = ""
        while num > 0:
            num, remainder = divmod(num,n) 
            res += punto[remainder]
        ans += res[::-1]
    return ans[p-1::m][:t]