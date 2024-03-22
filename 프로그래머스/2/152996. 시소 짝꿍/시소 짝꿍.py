from collections import Counter
def solution(weights):
    ans, count = 0, Counter(weights)
    for i in count:
        ans += count[i] * (count[i] - 1)//2
        ans += count[i] * count[i * 3/2]
        ans += count[i] * count[i * 2]
        ans += count[i] * count[i * 4/3]
    return ans