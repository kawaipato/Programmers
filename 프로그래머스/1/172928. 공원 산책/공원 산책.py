DIRS = {'N' : [-1,0], 'S' : [1,0], 'W' : [0,-1], 'E' : [0,1]}

def GO_r(park, now, go, num):
    raw_y, raw_x = now
    y, x = now
    for i in range(num):
        y, x = [a+b for a,b in zip(now, go)]
        try:
            if (park[y][x] != 'X') and (0<=y<len(park)) and (0<=x<len(park[0])):
                now = [y, x]
            else:
                return [raw_y,raw_x]
        except IndexError:
            return [raw_y,raw_x]
    return [y, x]

def solution(park, routes):
    for idx, p in enumerate(park):
        if 'S' in p:
            now = [idx,p.index('S')]
    for route in routes:
        go, num = route.split(" ")
        now = GO_r(park, now, DIRS[go], int(num))
    return now
