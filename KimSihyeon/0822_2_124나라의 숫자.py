def solution(n):
    answer = ''
    # 3진법 구하는 방식과 동일하게 while문 실행
    while n > 0:
        # 3으로 나눠떨어지지 않는 경우 3으로 나눈 나머지를 answer에 append (3진법 구하는 방식과 동일)
        if n % 3 != 0:
            answer += str(n % 3)
            n = n // 3
        # 3으로 나눠떨어지는 경우
        # 124나라에서는 '0'을 사용할 수 없으므로, 나머지가 (0,1,2가 아닌) '3'이 나오도록 몫을 낮춰 나눠줌 -> 후에 '3'을 '4'로 대치
        else:
            answer += '4'
            n = n // 3 - 1
    # n진법은 아래부터 위로 쓰니까 reverse string
    return answer[::-1]
