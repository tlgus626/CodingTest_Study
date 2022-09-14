def solution(arr):

    # 소수 리스트 지정
    sosu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    # count하는 리스트 생성
    count = [0] * len(sosu)

    # arr 내 숫자의 개수만큼 반복
    for num in arr:

        # 소수 리스트에서 대입할 거라 소수 리스트 반복 (소인수분해임)
        for i, a in enumerate(sosu):

            # 나중에 count 리스트에 저장할 cnt값
            cnt = 0

            # 소수로 안 나눠질 때까지 반복
            while num % a == 0:
                cnt += 1
                num //= a
            
            # 전체 숫자의 소인수 지수를 구할 수 있음
            # (최소공배수는 모든 숫자의 소인수 중 지수가 가장 큰 값을 전부 곱한 값)
            if cnt > count[i]: count[i] = cnt
    
    # 답을 출력하기 위한 값 answer는 1로 지정
    answer = 1

    # 각 소인수를 전부 곱하면 최소공배수
    for i, num in enumerate(sosu):
        answer *= num ** count[i]
        
    return(answer) # 괄호도 안 써도 될텐데 굳이 썼네