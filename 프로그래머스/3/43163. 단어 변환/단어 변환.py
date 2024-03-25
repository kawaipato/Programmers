def solution(begin, target, words):
    def dfs(now, step, visited):
        if now == target:
            return step
        min_step = float('inf')
        for word in words:
            if word not in visited and sum(a != b for a, b in zip(now, word)) == 1:
                visited.add(word)
                min_step = min(min_step, dfs(word, step + 1, visited))
                visited.remove(word)
        return min_step

    visited = set()
    return dfs(begin, 0, visited) if target in words else 0