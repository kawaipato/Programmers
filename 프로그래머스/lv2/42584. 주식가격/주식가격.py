from collections import deque
def solution(prices):
    ans = []
    prices = deque(prices)
    while len(prices) > 0:
        cnt, s = 0, prices.popleft()
        for p in prices:
            cnt += 1
            if s > p:
                break
        ans.append(cnt)
    return ans