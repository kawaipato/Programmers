def solution(n, computers):
    ans, visited = 0, []
    def new_root(i,n,visited):
        for j in range(n):
            if computers[i][j] == 1 and j not in visited:
                visited.append(j)
                new_root(j,n,visited)
    
    for i in range(n):
        if i not in visited:
            ans += 1
            visited.append(i)
            new_root(i,n,visited)
    return ans