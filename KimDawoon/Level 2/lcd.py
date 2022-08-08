def solution(arr):
    # 가장 큰 수를 지정
    n = max(arr)
    
    # all() : 모든 경우가 참일경우 True값 출력
    while True:
        if all(n % c == 0 for c in arr): # 모든수로 나누었을때 나머지가 0이어야 True
            break
        n+=1
    return n
