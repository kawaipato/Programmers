def solution(priorities, location):
    n = len(priorities)
    t = 0
    for i in range(n):
        while priorities[t%n] == 0 or priorities[t%n] < max(priorities):
            t += 1
        if t%n == location:
            return i + 1
        priorities[t%n] = 0
        print(priorities, t)