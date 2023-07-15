def solution(name, yearning, photo):
    sol_dict = dict(zip(name,yearning))
    scores = []
    for ph in photo:
        score = 0
        for p in ph:
            if p in sol_dict:
                score += sol_dict[p]
        scores.append(score)
    return scores