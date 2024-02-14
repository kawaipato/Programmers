def solution(numbers, target):
    K = (sum(numbers) - target)//2
    numL = len(numbers)
    def dfs(target, idx, cnt):
        for i in range(idx, numL):
            temp = target
            temp -= numbers[i]
            if temp == 0:
                cnt += 1
            elif temp > 0:
                cnt += dfs(temp, i+1, 0)
            else:
                continue
        return cnt
    
    return dfs(K, 0, 0)
        