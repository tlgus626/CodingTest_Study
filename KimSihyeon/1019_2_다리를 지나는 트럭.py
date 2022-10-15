# 트럭은 1초에 한 칸씩 지나간다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tq = [0] * bridge_length
    while tq:
        # 1초가 지났으니 트럭 한 대 나감
        answer += 1
        tq.pop(0)
        # 대기 트럭이 있다면
        if truck_weights:
            if sum(tq) + truck_weights[0] <= weight:
                tq.append(truck_weights.pop(0))
            else:
                tq.append(0)
    return answer
