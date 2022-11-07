# DFS를 활용한 순위 이진탐색 모범답안
from bisect import bisect_left, bisect_right

# DFS를 활용한 딕셔너리 만들기
def get_sihyeon_style_dfs(info, hashmap):
    
    # 스코어는 대소비교 해야하므로 따로 산출
    score = int(info.split(' ')[-1])
    
    # 스코어를 제외한 나머지 기준을 뽑아냄
    info = info.split(' ')[:-1]
    res = info.copy()
    
    def dfs(L):
        # 4개의 기준에 '-'을 허용해야 하므로 4번째 항목까지 '-'를 집어넣기 위해 반복
        if L == 4:
            key = ''.join(res)
            if bool(hashmap.get(key)):
                # 이미 존재할 시 작은 순서부터 투입
                hashmap[key].insert(bisect_left(hashmap[key],score),score)
            else:
                # 존재하지 않을시 처음 생성
                hashmap[key] = [score]
            return
        else:
            # '-'을 투입해 실행
            res[L] = '-'
            dfs(L+1)
            
            # 원래 기준 그대로 실행
            res[L] = info[L]
            dfs(L+1)
    dfs(0)
    return hashmap


def solution(info, query):
    
    # 받아들일 딕셔너리 생성
    hashmap = dict()
    
    # 모든 경우의 수를 담는 딕셔너리 생성
    for i in info:
        hashmap = get_sihyeon_style_dfs(i, hashmap)
    
    # 해쉬를 활용해 기준을 입력하면 기준에 맞는 참가자의 점수만 생성
    a = []
    for q in query:
        # 스코어 분리
        target_score = int(q.split(' ')[-1])
        q = ''.join(q.replace(' and ',' ').split(' ')[:-1])
        
        # 생성된 기준이 존재하면 스코어 기준을 넘는 사람의 인원수 출력
        if bool(hashmap.get(q)):
            a += [len(hashmap[q]) - bisect_left(hashmap[q],target_score)]
        
        # 기준이 생성된 적이 없으면 0명을 출력
        else:
            a += [0]
    return a
