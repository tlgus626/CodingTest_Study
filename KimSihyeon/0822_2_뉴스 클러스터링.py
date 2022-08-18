def solution(str1, str2):
    # 각 string을 집합으로 만들어주는 함수
    def getset(s):
        myset = []
        for i in range(len(s) - 1):
            e = s[i:(i + 2)]
            if e.lower().isalpha():
                myset.append(e.lower())
        return myset
    set1, set2 = getset(str1), getset(str2)

    # 두 중복집합의 교집합과 합집합 구하기
    # 전략 : 합집합 리스트에는 먼저 set1 원소를 다 넣어놓고, 이후 차집합(set2-set1) 원소만 넣어주기
    intersect, union = [], set1.copy()
    for s in set2:
        # set2의 원소가 set1에도 있음 == 교집합 (비교된 set1의 원소는 이제 필요 없음)
        if s in set1:
            intersect.append(s)
            set1.remove(s)
        # set2의 원소가 set1에는 없음 == 합집합
        else:
            union.append(s)

    if len(set1) == 0 and len(set2) == 0:
        return 65536
    else:
        return int(len(intersect) / len(union) * 65536)
