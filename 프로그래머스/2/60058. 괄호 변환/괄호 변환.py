def check(p):
    stack = []
    for char in p:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def divide(p):
    count = 0
    for i, char in enumerate(p):
        if char == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]

def solution(p):
    if not p:
        return ""

    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for ch in u[1:-1]:
            if ch == '(':
                answer += ')'
            else:
                answer += '('
        return answer
