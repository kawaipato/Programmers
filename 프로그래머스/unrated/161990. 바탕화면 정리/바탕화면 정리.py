def solution(wallpaper):
    L,m=[],[]
    for i, w in enumerate(wallpaper):
        if w.find('#') >= 0:
            L.append((i,w.find('#')))
            m.append(w.rfind('#'))
    print(L, m)
    return min([i[0] for i in L]), min([i[1] for i in L]), max([i[0] for i in L]) + 1, max(m) + 1