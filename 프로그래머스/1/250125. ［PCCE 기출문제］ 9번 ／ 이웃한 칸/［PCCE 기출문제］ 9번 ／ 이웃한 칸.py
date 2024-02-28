def solution(board, h, w):
    color,res, dirr = board[h][w] , 0, [[h-1,w],[h,w-1],[h+1,w],[h,w+1]]
    for new_h, new_w in dirr:
        if (0 <= new_h <= len(board)-1) and (0 <= new_w <= len(board[0])-1) and board[new_h][new_w] == color:
            res += 1
    return res
            