from collections import deque
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
def move(data, d, y, x):
    dy, dx = d
    while True:
        y += dy
        x += dx
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):    break
        if data[y][x] == 'D':   break
    return y - dy, x - dx
    
def bfs(start, end, data):
    visited = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
    visited[start[0]][start[1]] = 0
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        if [y, x] == end:  
            return visited[y][x]
        for d in DIRS:
            new_y, new_x = move(data, d, y, x)
            if visited[new_y][new_x] == -1:  
                queue.append([new_y, new_x])
                visited[new_y][new_x] = visited[y][x] + 1  
    return -1  
    
def search(data, c):
    for idx, d in enumerate(data):
        if c in d:
            return [idx, d.index(c)]
    return -1
def solution(board):
    start, end = search(board,'R'), search(board,'G')
    print(start, end)
    return bfs(start, end, board)
