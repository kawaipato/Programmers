def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    truck_weights = truck_weights[::-1]
    answer, now_weight = 0, 0
    while truck_weights:
        answer += 1
        now_weight -= bridge.pop(0)
        w = truck_weights.pop() if now_weight + truck_weights[-1] <= weight else 0
        now_weight += w
        bridge.append(w)
    return answer + bridge_length