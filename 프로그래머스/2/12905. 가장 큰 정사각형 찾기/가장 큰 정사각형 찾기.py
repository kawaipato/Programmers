def solution(board):
    if not board:   return 0
    max_length = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] >= 1:
                board[i][j] += min(board[i-1][j-1],board[i-1][j],board[i][j-1])
    for b in board: 
        if max_length < max(b): max_length = max(b)
    return max_length ** 2