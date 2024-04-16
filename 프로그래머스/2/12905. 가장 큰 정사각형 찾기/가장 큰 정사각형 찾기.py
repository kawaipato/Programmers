def solution(board):
    if not board:   return 0
    
    u, v = len(board), len(board[0])
    max_length = 0
    dp = [[0] * (v+1) for _ in range(u+1)]
    for i in range(1,u+1):
        for j in range(1,v+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
                max_length = max(max_length, dp[i][j])
    return max_length ** 2