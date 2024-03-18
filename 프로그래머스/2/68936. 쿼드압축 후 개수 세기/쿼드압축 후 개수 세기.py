def solution(arr):
    def quad_tree(x, y, n):
        first = arr[x][y]
        for i in range(n):
            for j in range(n):
                if first != arr[x+i][y+j]:
                    quad_tree(x,y,n//2)
                    quad_tree(x+n//2,y,n//2)
                    quad_tree(x,y+n//2,n//2)
                    quad_tree(x+n//2,y+n//2,n//2)
                    return
        ans[first] += 1
    ans = [0,0]
    quad_tree(0, 0, len(arr))
    return ans
