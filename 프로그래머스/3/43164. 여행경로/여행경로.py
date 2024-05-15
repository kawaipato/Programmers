from collections import defaultdict # 빈 key값에 빈 리스트 할당
def solution(tickets):
    def mapping(tickets):
        mapp = defaultdict(list)
        for i in range(len(tickets)):
            a, b = tickets[i]
            mapp[a].append((b,i))
        for city in mapp:
            mapp[city].sort()
        return mapp
    
    MAP = mapping(tickets)
    result = []
    visited = [False] * len(tickets)
    done = len(tickets) + 1
    def dfs(city, path):
        nonlocal done, visited, MAP, result
        if result:
            return
        if len(path) == done:
            result = path.copy()
            return
        for new_city, new_i in MAP[city]:
            if visited[new_i]:
                continue
            visited[new_i] = True
            path.append(new_city)
            dfs(new_city,path)
            path.pop()
            visited[new_i] = False
            
        
    dfs('ICN',['ICN'])
    return result