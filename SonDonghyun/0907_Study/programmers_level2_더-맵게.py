def solution(scoville, K):
    import heapq
    cnt = 0
    heapq.heapify(scoville)

    if len(scoville) == 2:
        return 1
        
    min_scov1 = heapq.heappop(scoville)

    while len(scoville) >= 1:
        min_scov2 = heapq.heappop(scoville)
        new_food = min_scov1 + min_scov2 * 2

        min_scov1 = heapq.heappop(scoville)
        cnt += 1
        heapq.heappush(scoville, new_food)
    
        if new_food >= K and min_scov1 >= K:
            break

    if new_food < K and min_scov1 < K:
        cnt = -1
    
    return cnt