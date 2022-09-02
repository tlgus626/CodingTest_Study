import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        # 가장 맵지 않은 음식의 스코빌지수
        s0 = heapq.heappop(scoville)
        # 제일 안 매운 게 이미 K 이상이므로 while문 break
        if s0 >= K:
            break
        # 계속 섞다보니 s0가 마지막 남은 음식.. 그런데 K를 못넘으니까 -1 리턴
        if len(scoville) == 0:
            return -1
        # 두번째 맵지 않은 음식의 스코빌지수
        s1 = heapq.heappop(scoville)
        # 음식 섞음, 섞은 횟수+1번
        heapq.heappush(scoville, s0 + (s1 * 2))
        answer += 1
    return answer
