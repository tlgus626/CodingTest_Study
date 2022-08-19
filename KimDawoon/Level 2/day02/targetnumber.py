def solution(numbers, target):
    
    # 답을 받아드리는 변수
    k = 0
    
    # 깊이 우선 탐색
    def DFS(sum, idx):
        # solution안에 있는 k를 선언
        nonlocal k
        # 길이가 같으면 target을 비교 후, 같으면 k를 1 증가
        if idx == len(numbers):
            if sum == target:
                k += 1
            # k에 저장했기 때문에 return값이 존재하지 않아도 실행 가능
            return 
        # 값을 적용하여 다시 깊이 탐색
        DFS(sum + numbers[idx], idx+1)
        DFS(sum - numbers[idx], idx+1)
    
    # 함수 적용
    DFS(0,0)
    return k
