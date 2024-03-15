import re
from itertools import product
def solution(user_id, banned_id):
    ans = []
    for id in banned_id:
        id = id.replace('*','.')
        res = []
        for u_id in user_id:
            match = re.fullmatch(id,u_id)
            if match:
                res.append(u_id)
        ans.append(res)
    answer, pl = list(product(*ans)), []
    for a in answer:
        if len(set(a)) == len(banned_id):
            pl.append(a)
    return len(set(tuple(sorted(item)) for item in pl))
