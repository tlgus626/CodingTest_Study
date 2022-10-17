# 이 문제에 너무 시간을 많이 써서 다른 사람 풀이 참고
from collections import deque

def solution(bridge_length, weight, truck_weights):

    on_bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    
    time = 0
    total = 0 # 다리 위에 남아있는 트럭의 무게 합

    while waiting:

        time += 1
        total -= on_bridge[0] # 나갈 트럭이니까 total에서 무게 빼줌
        on_bridge.popleft()

        if total + waiting[0] > weight:
            on_bridge.append(0)
        else:
            truck = waiting.popleft()
            total += truck # 다링 위에 새로 온 트럭 무게 더해줌
            on_bridge.append(truck)

    return time + bridge_length
