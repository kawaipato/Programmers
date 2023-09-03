def solution(priorities, location):
    ans,c = 0, 0
    best = sorted(priorities, reverse=True)
    while True:
        for i, p in enumerate(priorities):
            b = best[c]
            if p == b:
                c += 1
                ans += 1
                if i == location:
                    break
        else:
            continue
        break
    return ans