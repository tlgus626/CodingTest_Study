def solution(n):

    # n번째 피보나치 수를 저장하는 리스트
    dp = [0]*(n+1)

    # initialize
    dp[0] = 0
    dp[1] = 1

    # dynamic programming
    for i in range(2,n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    answer = dp[n] % 1234567
    return answer