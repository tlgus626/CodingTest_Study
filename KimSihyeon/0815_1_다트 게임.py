def solution(dartResult):

    # 나중에 숫자 10을 string에서 인덱싱하기 어려우므로 %으로 치환
    dartResult = dartResult.replace('10', '%')

    answer = []

    for i in range(len(dartResult)):
        d = dartResult[i]

        # d가 숫자인 경우는 우선 지나치고, 보너스(S/D/T)인 경우에만 answer에 점수 append
        if d.isalpha():

            # 기본 점수(0~10점)
            if dartResult[i-1] == '%': n = 10
            else: n = int(dartResult[i - 1])

            # 보너스에 따라 최종 점수 append
            if d == 'S': answer.append(n)
            elif d == 'D': answer.append(n ** 2)
            elif d == 'T': answer.append(n ** 3)

        # 옵션 1.스타상
        elif d == '*':
            answer[-1] = answer[-1] * 2
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2 # 아직 아무 점수도 획득하지 않았다면 직전 점수를 두배 곱할 수 없음.

        # 옵션 2.아차상
        elif d == '#':
            answer[-1] = answer[-1] * (-1)

    return sum(answer)