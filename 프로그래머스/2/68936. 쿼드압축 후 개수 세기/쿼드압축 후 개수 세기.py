def solution(arr):
    def quad_tree(arr, a, n):
        x, y, number = a[0], a[1], arr[a[0]][a[1]]
        result = [0, 0]
        for i in range(n):
            for j in range(n):
                if number != arr[x+i][y+j]:
                    r1 = quad_tree(arr,[x,y],n//2)
                    r2 = quad_tree(arr,[x+n//2,y],n//2)
                    r3 = quad_tree(arr,[x,y+n//2],n//2)
                    r4 = quad_tree(arr,[x+n//2,y+n//2],n//2)
                    result = [r1[i]+r2[i]+r3[i]+r4[i] for i in range(2)]
                    return result
        result[number] += 1
        return result
    a = [0,0]
    res = quad_tree(arr, a, len(arr))
    return res
