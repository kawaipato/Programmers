import numpy as np
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [i,j] != [0,0] and not [j+1,i+1] in puddles:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[-1][-1] % 1000000007