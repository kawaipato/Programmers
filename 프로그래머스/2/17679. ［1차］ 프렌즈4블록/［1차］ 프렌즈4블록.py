answer = 0
def solution(m, n, board):
    global answer
    sb = search_block(m,n,board)
    if len(sb) != 0:
        new_b = remove_block(sb, board)
        new_b2 = arrange_block(m,n,new_b)
        solution(m,n,new_b2)
    return answer
    
def search_block(m,n,board):
    remove = []
    for i in range(m-1):
        for j in range(n-1):
            now = board[i][j]
            if now != '.' and now == board[i][j+1] and now == board[i+1][j] and now == board[i+1][j+1]:
                if [i,j] not in remove:   remove.append([i,j])
                if [i,j+1] not in remove:   remove.append([i,j+1])
                if [i+1,j] not in remove:   remove.append([i+1,j])
                if [i+1,j+1] not in remove:   remove.append([i+1,j+1])
    return remove

def remove_block(sb, board):
    global answer
    for k in range(len(sb)):
        m, n = sb[k]
        board[m] = board[m][:n] + '.' + board[m][n+1:]
    answer += len(sb)
    return board

def arrange_block(m,n,board):
    bt = [''.join(x).replace('.','') for x in zip(*board)]
    for idx, b in enumerate(bt):
        if len(b) < m:
            bt[idx] = '.' * (m - len(b)) + bt[idx]
    bt = [''.join(x) for x in zip(*bt)]
    return bt