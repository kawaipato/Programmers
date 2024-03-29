def solution(genres, plays):
    music,idx,answer, full = {},0,[], []
    for genre, play in zip(genres, plays):
        if genre not in music:
            music[genre] = 0
        music[genre] += play
    sorted_music = sorted(music.items(), key=lambda x: x[1], reverse=True)
    for genre, _ in sorted_music:
        tmp = []
        for idx, (g, p) in enumerate(zip(genres,plays)):
            if genre == g:
                tmp.append((idx,p))
        tmp = sorted(tmp, key = lambda x : (-x[1],x[0]))
        answer += [t[0] for t in tmp[:2]]
    return answer