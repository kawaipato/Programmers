def solution(numbers):
    ans, stack = [-1] * len(numbers), []
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            ans[stack.pop()] = num
        stack.append(idx)
    return ans