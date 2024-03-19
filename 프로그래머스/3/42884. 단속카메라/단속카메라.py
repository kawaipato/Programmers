def solution(routes):
    routes.sort(key = lambda x: (x[0],x[1]))
    now, answer = routes[0][1], 0
    for route in routes:
        if route[0] > now:
            now = route[1]
            answer += 1
        else:
            now = min(route[1],now)
    return answer + 1