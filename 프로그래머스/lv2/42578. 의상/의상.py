from collections import Counter
def solution(clothes):
    clothes = [cloth[1] for cloth in clothes]
    wow, ans = list(Counter(clothes).values()), 1
    for w in wow:
        ans *= w + 1
    return ans - 1