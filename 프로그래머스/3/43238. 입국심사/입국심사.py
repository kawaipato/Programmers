def solution(n, times):
    def check(times, takeTimes, people):
        now = 0
        for time in times:
            now += takeTimes // time
        return True if now >= people else False
    def binary_search(people, times):
        l = 1
        r = times[-1] * people
        minTimes = r
        while l <= r:
            mid = (l+r) // 2
            if check(times, mid, people):
                minTimes = mid
                r = mid - 1
            else:
                l = mid + 1
        return minTimes

    times.sort()
    timer = binary_search(n,times)
    return timer
    
                
                