import re
def solution(dartResult):
    prizes = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    darts = re.findall('(\d+)([SDT])([*#]?)' ,dartResult)
    scores = [0] * 3
    for i, (score, op, prize) in enumerate(darts):
        if prize == '*' and i > 0:
            scores[i - 1] *= 2
        scores[i] = int(score) ** prizes[op] * option[prize]
    return sum(scores)
        
        