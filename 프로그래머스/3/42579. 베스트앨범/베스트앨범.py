def solution(genres, plays):
    music, idx, answer, full = {}, 0, [], []
    
    # 각 장르에 대한 정보를 딕셔너리에 저장
    for genre, play in zip(genres, plays):
        if genre not in music:
            music[genre] = 0
        music[genre] += play
        
    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    sorted_music = sorted(music.items(), key=lambda x: x[1], reverse=True)
    
    # 각 장르별로 최대 2곡씩 베스트 앨범에 추가
    for genre, _ in sorted_music:
        tmp = []
        for i, (g, p) in enumerate(zip(genres, plays)):
            if g == genre:
                tmp.append((i, p))
        tmp = sorted(tmp, key=lambda x: (-x[1], x[0]))  # 재생 횟수가 동일할 때 고유 번호로 정렬
        answer.extend([t[0] for t in tmp[:2]])  # 최대 2곡 추가
    return answer