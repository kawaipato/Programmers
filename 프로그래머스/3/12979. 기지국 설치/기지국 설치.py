import math
def solution(n, stations, w):
    floor, now, answer = [], 0, 0
    for station in stations:
        first, last = max(1,(station-w)), min((station+w),n)
        if now < first:
            answer += math.ceil((first - now - 1)/(w*2 + 1))
        now = last
    if last < n:
        answer += math.ceil((n - now)/(w*2 + 1))
    return answer
            