def solution(x, y, n):
    INF = float('inf')
    maxa = 1000000 + 1
    dp = [INF] * (y + 1)
    
    dp[x] = 0
    
    for cal in range(x,y):
        if dp[y] != INF:
            return dp[y]
        
        for nn in (cal * 2, cal * 3, cal + n):
            if y < nn:
                continue
                
            dp[nn] = min(dp[nn], dp[cal] + 1)
    return dp[y] if dp[y] != INF else -1
                