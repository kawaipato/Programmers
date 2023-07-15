from collections import Counter
def solution(k, tangerine):
    a, b =Counter(tangerine).most_common(), 0
    for i in range(len(a)):
        b += a[i][1]
        if b >= k:
            return i+1
            break
    