def solution(record):
    act, name, res = [], {}, []
    for r in record:
        a = r.split()
        act += [a[:2]]
        if len(a) == 3:
            name[a[1]] = a[2]
    for a in act:
        if a[0] == 'Enter':
            res.append(f'{name[a[1]]}님이 들어왔습니다.')
        elif a[0] == 'Leave':
            res.append(f'{name[a[1]]}님이 나갔습니다.')
        else:
            continue
    return res