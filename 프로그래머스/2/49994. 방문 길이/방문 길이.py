def solution(dirs):
    rule = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    x, y, s = 0, 0, set()
    for i in dirs:
        nx, ny = x + rule[i][0], y + rule[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
