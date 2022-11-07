# DFS 성공

# global로 지정해줄 cnt
cnt = 0

def solution(numbers, target):

    def dfs(level, value):
    
        global cnt # 함수 외부 변수인 cnt 업데이트 할 수 있도록 global 사용
    
        if level == len(numbers): # level이 리스트 길이랑 같아지면 결과 업데이트 하고 return
        
            if value == target: # cnt 업데이트 조건: 계산한 값이 target 값과 같아질 때
                cnt += 1
        
            return

        # 재귀로 +한 결과와 -결과가 각각 뻗어나가도록 함
        dfs(level + 1, value + numbers[level])
        dfs(level + 1, value - numbers[level])
    
    # 정의한 dfs 함수 사용: level = 0, target = 0
    dfs(0, 0)
    
    return cnt