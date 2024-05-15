from collections import defaultdict # 빈 key값에 빈 리스트 할당
def solution(tickets):
    MAP = defaultdict(list)
    for a, b in tickets:
        MAP[a].append(b)
    for m in MAP.keys():
        MAP[m].sort()

    path, res = ["ICN"], []
    while path:
        now = path[-1]
        if MAP[now]:
            path.append(MAP[now].pop(0))
        else:
            res.append(path.pop())
    return res[::-1]