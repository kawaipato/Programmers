def solution(routes):
    routes.sort(key = lambda x : x[1])
    last_camera, answer = -30001, 0
    for route in routes:
        if last_camera < route[0]:
            last_camera = route[1]
            answer += 1
    return answer