def solution(priorities, location):

    from collections import deque
    d = deque(priorities)
    cnt = 0

    while d: # 리스트가 빌 때까지 반복

        # 큐의 첫번째 원소만 계속 확인

        if d[0] == max(d): # 중요도 높아서 출력

            cnt += 1 # 출력 순서 카운트
            d.popleft() # 첫번째 원소 출력

            if location == 0:
                break
            else: location -= 1

        else: # 중요도 낮아서 넘김

            d.append(d[0])
            d.popleft()

            if location == 0: location = len(d) - 1
            else: location -= 1
        
    return cnt