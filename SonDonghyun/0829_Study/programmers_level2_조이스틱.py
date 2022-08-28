def solution(name):

    if set(name) == {'A'}:
        return 0

    answer = float('inf')

    # 한 쪽으로 갔다가 다시 반대쪽으로 움직였을 때를 고려하기 위한 반복
    for i in range(len(name) // 2): # 고로 전체 문자열의 반 이상 움직일 필요 없음

        left_moved = name[-i:] + name[:-i] # 왼쪽으로 이동하다가 오른쪽으로 이동하는 것을 고려하려고 사용
        right_moved = name[i:] + name[:i] # 오른쪽으로 이동하다가 왼쪽으로 이동하는 것을 고려하려고 사용

        # 왼->오, 오->왼을 모두 고려
        for n in [left_moved, right_moved[0] + right_moved[:0:-1]]:

            # 마지막 글자가 A가 아닐 때까지 우측에서 한칸씩 줄임
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n) - 1 # i는 한쪽으로 움직인 카운트, len(n) - 1이 다시 반대쪽으로 움직였을 때 카운트
            
            # 상하 움직임 카운트
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer