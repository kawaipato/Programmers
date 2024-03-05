def solution(players, callings):
    dic_play = {player : idx for idx, player in enumerate(players)}
    for c in callings:
        i = dic_play.get(c)
        front = players[i - 1]
        dic_play[c], dic_play[front] = i - 1, i
        players[i-1] = players[i]
        players[i] = front
    return players