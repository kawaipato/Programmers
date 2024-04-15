def check(p):
    now = 0
    for pp in p:
        if pp == '(':
            now += 1
        else:
            if now <= 0:
                return False
            now -= 1
    return now == 0
def divide(p):
    cnt = 0
    for idx, pp in enumerate(p):
        if pp == ')':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:idx+1], p[idx+1:]

def solution(p):
    if p == '': return ''
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for uu in u[1:-1]:
            if uu == ')': answer += '('
            else:   answer += ')'
        return answer
        