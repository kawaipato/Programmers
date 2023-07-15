def solution(people, limit):
    a = sorted(people)
    j,cnt = len(a) - 1, 0
    i=0
    while i <= j:
        if a[i] + a[j] > limit:
            j -= 1
            cnt += 1
        else:
            cnt += 1
            i += 1
            j -= 1
    return cnt