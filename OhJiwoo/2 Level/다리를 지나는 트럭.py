from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque([0]*bridge_length)
    orders = deque(truck_weights)
    time=0
    total=0
    while orders:
        time+=1
        total -= queue[0]
        queue.popleft()
        if total + orders[0] > weight:
            queue.append(0)
        else:
            w = orders.popleft()
            total+=w
            queue.append(w)

    return time+bridge_length
