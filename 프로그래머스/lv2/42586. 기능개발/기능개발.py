def solution(progresses, speeds):
    cnt,t = 0, 0
    lst = []
    while len(progresses) > 0:
        if progresses[0] + t * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                lst.append(cnt)
                cnt = 0
            t += 1
    lst.append(cnt)
    return lst
    