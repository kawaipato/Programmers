Go = {0 : (1,0), 1: (0,1), 2 : (-1,-1)}
def solution(n):
    triangle = [[0] * i for i in range(1,n+1)]
    x,y,num=-1,0,1
    for i in range(n):
        for _ in range(i,n):
            go_x, go_y = Go[i % 3]
            x, y = x + go_x, y + go_y
            triangle[x][y] = num
            num += 1
    return sum(triangle,[])