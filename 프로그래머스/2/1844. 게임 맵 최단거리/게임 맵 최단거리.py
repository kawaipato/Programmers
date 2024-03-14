from collections import deque
def solution(maps):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    def new_block(x,y):
        now = deque()
        now.append((x,y))
        while now:
            x, y = now.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if new_x < 0 or new_y < 0 or new_x >= len(maps) or new_y >= len(maps[0]):
                    continue
                elif maps[new_x][new_y] == 0:
                    continue
                elif maps[new_x][new_y] == 1:
                    now.append((new_x,new_y))
                    maps[new_x][new_y] = maps[x][y] + 1
    new_block(0,0)
    ans = maps[-1][-1]
    if ans == 1:
        ans = -1
    return ans