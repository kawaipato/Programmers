DIRS = {(0,1),(0,-1),(1,0),(-1,0)}
def bfs(data, start, w, second):
    visited = [start]
    queue = [[start[0], start[1], second]]
    while queue:
        y, x, s = queue.pop(0)
        if data[y][x] == w:
            return [y,x,s]
        for yy, xx in DIRS:
            s_y, s_x = y + yy, x + xx
            if (0 <= s_y < len(data)) and (0 <= s_x < len(data[0])) and data[s_y][s_x] != 'X':
                if [s_y,s_x] not in visited:
                    visited.append([s_y,s_x])
                    queue.append([s_y,s_x,s+1])
    return -1
                    
def search(data, where):
    for idx, d in enumerate(data):
        if where in d:
            return [idx, d.index(where)]
    return -1
def solution(maps):
    start = search(maps,'S')
    second = 0
    # search Lever
    lava = bfs(maps, start, 'L', second)
    if lava == -1:
        return -1
    result = bfs(maps, [lava[0],lava[1]], 'E', lava[2])
    if result == -1:
        return -1
    return result[-1]