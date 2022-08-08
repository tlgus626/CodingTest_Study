def solution(arr):

    # 수 x와 y의 최소공배수 구하는 함수
    def myftn(x, y, n=1):
        # 수 x와 y의 최대공약수
        for i in range(1, min(x, y) + 1):
            if x % i == 0 and y % i == 0:
                n = i
        # 수 x와 y의 최소공배수 = 두 수의 곱 // 최대공약수
        return (x * y) // n

    # 두 개의 최소공배수를 반복하여 구하기
    answer = 1
    for a in arr:
        answer = myftn(a, answer)

    return answer