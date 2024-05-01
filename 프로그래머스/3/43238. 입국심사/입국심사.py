def solution(n, times):
    start, end = 1, times[-1] * n
    while start < end:
        mid = (start + end) // 2
        now = 0
        for time in times:
            now += mid // time
        if now >= n:
            end = mid
        else:
            start = mid + 1
    return start