DIRS = ((-1,0),(1,0),(0,-1),(0,1))
def solution(maps):
    ans, width, vert = [], len(maps[0]), len(maps)
    visited = [[False] * width for _ in range(vert)]
    def dfs(x,y,counts):
        nonlocal visited
        start = [(x,y)]
        visited[y][x] = True
        now = counts
        while start:
            now_x, now_y = start.pop()
            for ax, ay in DIRS:
                new_x, new_y = now_x + ax, now_y + ay
                if 0 <= new_x < width and 0 <= new_y < vert and maps[new_y][new_x] != 'X' and not visited[new_y][new_x]:
                    visited[new_y][new_x] = True
                    now += int(maps[new_y][new_x])
                    start.append((new_x,new_y))
        return now
    
    
    for yy in range(vert):
        for xx in range(width):
            if maps[yy][xx] != 'X' and not visited[yy][xx]:
                ans.append(dfs(xx,yy,int(maps[yy][xx])))
    return sorted(ans) if ans else [-1]