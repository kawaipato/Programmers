def solution(order):
    extra, answer = [], 0
    for box in range(1, len(order) + 1):
        extra.append(box)
        while extra and extra[-1] == order[answer]:
            extra.pop(-1)
            answer += 1
    return answer
    