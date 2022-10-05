from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    people = defaultdict(list)
    for i in info:
        person = i.split()
        score = int(person[-1])
        people[''.join(person[:-1])].append(score)
        for j in range(4):
            candi = list(combinations(person[:-1], j))
            for c in candi:
                people[''.join(c)].append(score)
    for i in people:
        people[i].sort() # 이진 탐색을 사용하기 위한 정렬 
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key])-bisect.bisect_left(people[key], score))
    return answer
