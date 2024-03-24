from collections import Counter
def solution(gems):
    gem_len, ans = len(set(gems)), [0,0]
    now, ans_lst = Counter(), []
    for idx, gem in enumerate(gems):
        ans[1] += 1
        now[gem] += 1
        while len(now) == gem_len:
            now[gems[ans[0]]] -= 1
            if now[gems[ans[0]]] == 0:
                del now[gems[ans[0]]]
            ans[0] += 1
            ans_lst.append([ans[0],idx+1])

    return sorted(ans_lst, key = lambda x: (x[1]-x[0], x[0]))[0]
    