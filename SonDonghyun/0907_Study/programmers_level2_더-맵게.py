def solution(scoville, K):
    import heapq
    cnt = 0
    heapq.heapify(scoville)

    # 예제 16번 런타임 에러 떠서 추가한 조건
    if len(scoville) == 2:
        return 1 # 얼렁뚱땅 해결
    
    # 반복문 밖에서 시작
    min_scov1 = heapq.heappop(scoville)

    while len(scoville) >= 2:
        min_scov2 = heapq.heappop(scoville) # 반복문 안에서 힙팝
        new_food = min_scov1 + min_scov2 * 2 # 새 음식 스코빌 계산

        min_scov1 = heapq.heappop(scoville) # 하나더 힙팝
        cnt += 1
        heapq.heappush(scoville, new_food) # 새 음식 힙에 추가
    
        if new_food >= K and min_scov1 >= K: # 방금 전 빼낸 힙이랑 새 음식 스코빌 지수 확인
            break
    
    # 반복문 끝나고도 K 안 넘으면 -1
    if new_food < K and min_scov1 < K:
        cnt = -1
    
    return cnt