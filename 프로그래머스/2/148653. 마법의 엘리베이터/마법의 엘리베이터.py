def solution(storey):
    answer = 0
    while storey != 0:
        storey, imsi = divmod(storey, 10)
        if imsi > 5 or (imsi == 5 and (storey % 10) >= 5):
            imsi = 10 - imsi
            storey += 1
        answer += imsi
    return answer