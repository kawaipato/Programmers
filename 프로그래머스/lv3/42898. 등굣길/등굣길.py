def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            if [x,y] != [0,0] and not [x+1,y+1] in puddles:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return dp[-1][-1] % 1000000007