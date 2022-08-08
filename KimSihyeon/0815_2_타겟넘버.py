cnt = 0

def solution(numbers, target) :
    # DFS 재귀 함수
    def DFS(I, L) :
        global cnt
        # numbers의 모든 수를 다 탐색한 경우
        if I==len(numbers) :
            # 모든 수 탐색 결과, L이 타겟 넘버와 같다면 경우의 수 + 1
            if L==target :
                cnt += 1
                return
        # numbers의 모든 수를 탐색하는 과정
        else :
            DFS(I+1, L+numbers[I]) # I번째 수를 더하는 경우
            DFS(I+1, L-numbers[I]) # I번째 수를 빼는 경우

    # 함수 run
    DFS(0, 0)

    return cnt