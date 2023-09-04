import re
def solution(dartResult):
    darts = re.findall('(\d+)([SDT])([*#]?)' ,dartResult)
    scores = [0] * 3
    for i, (score, op, prize) in enumerate(darts):
        scores[i] = int(score)
        if op == 'D':
            scores[i] **= 2
        elif op == 'T':
            scores[i] **= 3
        if prize == '*':
            scores[i] *= 2
            if i > 0:
                scores[i-1] *= 2
        elif prize == '#':
            scores[i] *= -1
    return sum(scores)
        
        