import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    count =0
    while (scoville[0]<K and len(scoville)>1):
        hq.heappush(scoville, hq.heappop(scoville)+(hq.heappop(scoville)*2))
        count +=1
    if scoville[0] <K :
        return -1
    return count
