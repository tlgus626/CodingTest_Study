from collections import deque

def solution(progresses, speeds):
    # 작업진도와 속도를 큐 구조로 바꿈
    dq = deque(progresses)
    sq = deque(speeds)

    answer = []
    # 모든 작업이 끝날 때까지 while문 반복
    while dq :
        # 반복문 한 번 돌때마다 작업 속도만큼 작업 진도 증가
        for i in range(len(dq)) :
            dq[i] += sq[i]

        # 앞 기능이 먼저 배포가 가능해야 함
        if dq[0] >= 100 :
            dq.popleft()
            sq.popleft()
            # 배포
            cnt = 1
            # 뒷 기능들도 배포가 가능하다면 바로 배포
            for _ in range(len(dq)) :
                if dq[0] >= 100 :
                    dq.popleft()
                    sq.popleft()
                    cnt += 1
            answer.append(cnt)

    return answer