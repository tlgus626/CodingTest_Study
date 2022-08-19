def solution(str1, str2):

    # 주어진 문자열이 영문인 경우에만 리스트에 소문자로 저장
    s1 = [str1[i: i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    s2 = [str2[i: i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    # 중복조합을 해결하기 위한 과정
    # 리스트 내에 같은 문자가 있으면 느낌표를 하나씩 추가하는 방식 도입
    for i, word1 in enumerate(s1):
        for j, word2 in enumerate(s1):
            if i < j and word1 == word2:
                s1[j] = word2 + '!'

    for i, word1 in enumerate(s2):
        for j, word2 in enumerate(s2):
            if i < j and word1 == word2:
                s2[j] = word2 + '!'
    
    len_inter, len_union = len(set(s1) & set(s2)), len(set(s1) | set(s2))
    
    # 합집합이 공집합이면 1로 계산
    if len_union == 0: len_union, len_inter = 1, 1
    
    return int(len_inter / len_union * 65536)