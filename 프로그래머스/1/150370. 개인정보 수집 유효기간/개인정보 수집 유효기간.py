import datetime as dt
def solution(today, terms, privacies):
    ans, term = [], {alp : int(num) for alp, num in [t.split(' ') for t in terms]}
    today = [int(t) for t in today.split('.')]
    for idx, privacy in enumerate(privacies):
        p_date, alp = privacy.split(' ')
        p_date = [int(p) for p in p_date.split('.')]
        y, m = term[alp]//12, term[alp]%12
        p_date[0] += y
        p_date[1] += m
        if p_date[1] > 12:
            p_date[0] += 1; p_date[1] -= 12
        p_date[2] -= 1
        if p_date[2] == 0:
            p_date[1] -= 1; p_date[2] = 28
        if p_date[1] == 0:
            p_date[0] -= 1; p_date[1] = 12
        if dt.datetime(p_date[0],p_date[1],p_date[2]) < dt.datetime(today[0],today[1],today[2]):
            ans.append(idx+1)
    return ans   