from collections import deque
def solution(stones, k):
    ans, jump = float('inf'), deque()
    for idx, stone in enumerate(stones):
        while jump:
            if jump[0][0] <= idx - k:
                jump.popleft()
            elif jump[-1][1] < stone:
                jump.pop()
            else:   break
        jump.append((idx,stone))
        if idx + 1 >= k:
            ans = min(ans,jump[0][1])
    return ans