# 힙
import heapq as hq

def solution(scoville, K):
    
    cnt = 0
    # 리스트를 힙큐로 변환
    hq.heapify(scoville)
    q = scoville
    
    # 무한 반복
    while True:
        # 지수가 0이면 섞을 필요가 없음
        if K==0:
            return 0
        
        # 아무리 섞어도 길이가 1이면 만들 수 없음
        elif len(q) == 1:
            return -1
        
        # 섞기
        mix = hq.heappop(q) + hq.heappop(q)*2
        
        # 섞은 후 다시 큐에 저장
        hq.heappush(q,mix)
        
        # 섞은 횟수 저장
        cnt += 1
        
        # 최소값이 지수 이상이면 그만
        if q[0] > K:
            break
    
    return cnt
