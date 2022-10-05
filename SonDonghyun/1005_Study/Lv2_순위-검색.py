from bisect import bisect_left

def solution(info, query):
    
    # 가능한 모든 조건을 딕셔너리의 key로 추가, value는 list
    all_dict = {a + b + c + d:[] for a in ['cpp', 'java', 'python', '-'] for b in ['backend', 'frontend', '-'] for c in ['junior', 'senior', '-'] for d in ['pizza', 'chicken', '-']}

    # 위에 만든 딕셔너리에 지원자의 조건인 key에 코딩테스트 점수를 value로 append
    for i in info:
        this = i.split()[:4]
        for a in [this[0], '-']:
            for b in [this[1], '-']:
                for c in [this[2],'-']:
                    for d in [this[3], '-']:
                        all_dict[a + b + c + d].append(int(i.split()[-1]))

    # 딕셔너리의 모든 value를 sort (이진검색을 위해서)
    for i, j in all_dict.items():
        all_dict[i] = sorted(j)

    # bisect_left라는 이진검색 함수로 검색 (시간효율성)
    result = [0] * len(query)
    for i, q in enumerate(query):
        comp, score = ''.join(q.replace('and', '').split()[:4]), int(q.split()[-1])
        result[i] += len(all_dict[comp]) - bisect_left(all_dict[comp], score) # 길이에서 bisect_left 인덱스 빼주면 score보다 큰 사람 확인 가능

    return result