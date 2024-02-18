def solution(n, works):
    from collections import Counter
    lst = [list(item) for item in sorted(Counter(works).items())]
    while n > 0:
        time, amount = lst.pop(-1)
        if n >= amount:
            if lst and lst[-1][0] == time - 1:
                lst[-1][1] += amount
            else:
                lst.append([time-1,amount])
            n -= amount
        else:
            if lst and lst[-1][0] == time - 1:
                lst[-1][1] += n
            else:
                lst.append([time-1,n])
            lst.append([time,amount-n])
            n -= amount
    if lst[-1][0] <= 0: return 0
    ans = 0
    for time, amount in lst:
        ans += amount * time ** 2
    return ans