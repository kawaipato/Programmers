def solution(boards, moves):
    result, stack = 0, []
    for move in moves:
        for idx, board in enumerate(boards):
            if board[move-1] != 0: # 만약에 순차적으로 행을 봤을때, 숫자가 있다면..
                if stack and board[move-1] == stack[-1]: # stack에 같은 숫자가 있으면
                    result += 2
                    del stack[-1] # 두개의 겹쳐진 숫자 삭제~
                else: # stack이 비어있는데 숫자를 찾으면
                    stack.append(board[move-1])
                boards[idx][move-1] = 0
                break
    return result
                    
    