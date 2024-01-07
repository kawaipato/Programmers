from collections import Counter
def solution(topping):
    ans, chulsoo = 0, set()
    bro = Counter(topping)
    for t in topping:
        bro[t] -= 1
        if bro[t] == 0:
            del bro[t]
        chulsoo.add(t)
        if len(bro) == len(chulsoo):
            ans += 1
    return ans
    