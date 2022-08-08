def solution(n, lost, reserve):

    # n명의 학생들에게 체육복이 몇 개 있는지 확인하는 리스트
    check = [0]*(n+1)

    for i in range(1, n+1) :
        # 도난도 당하고, 여벌 체육복도 있는 학생
        if i in lost and i in reserve :
            check[i] = 1
        # 도난 당한 학생
        elif i in lost :
            check[i] = 0
        # 여벌 체육복이 있는 학생
        elif i in reserve :
            check[i] = 2
        # 기타 : 체육복 1벌인 학생
        else :
            check[i] = 1
    # 마지막 사람이 lost인 경우, check[n+1]을 확인할 수 없기 때문에 n까지 확인
    for i in range(1, n) :
        if check[i] == 0 :
            # 잃어버린 학생의 왼쪽 학생이 여벌 가지고 있는 경우
            if check[i-1] == 2 :
                check[i] += 1
                check[i-1] -= 1
            # 잃어버린 학생의 오른쪽 학생이 여벌 가지고 있는 경우
            elif check[i+1] == 2 :
                check[i] += 1
                check[i+1] -= 1
    # check가 0보다 큼 i.e., 체육복이 있어서 수업을 들을 수 있음
    answer = 0
    for c in check :
        if c > 0 :
            answer += 1

    return answer