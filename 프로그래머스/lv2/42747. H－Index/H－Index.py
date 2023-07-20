def solution(citations):
    answer = 0
    s = sorted(citations,reverse=True)
    for i in s:
        if i > answer:
            answer += 1
    return answer