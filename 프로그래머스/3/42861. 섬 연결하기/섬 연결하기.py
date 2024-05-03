
def solution(n, costs):
    islands = [i for i in range(n+1)]
    costs.sort(key=lambda x : x[2])
    SUM = 0
    def find_islands(a):
        if islands[a] == a:  return a
        else:
            islands[a] = find_islands(islands[a])
            return islands[a]
    def union_islands(a, b):
        x = find_islands(a)
        y = find_islands(b)
        if x != y:
            islands[x] = y
            
    for a, b, cost in costs:
        if find_islands(a) != find_islands(b):
            union_islands(a, b)
            SUM += cost
    return SUM