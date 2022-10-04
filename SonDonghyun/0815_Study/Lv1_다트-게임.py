def solution(dartResult):
    
    if '10' in dartResult: dartResult = dartResult.replace('10', 't') # 10은 0이나 1이랑 겹칠 것 같아서 다른 문자로 교체
    
    # 치환할 문자열 리스트 생성 (딕셔너리로 해도 됨)
    word_list = [str(i) for i in range(10)]+['t']+['S', 'D', 'T', '#', '*']
    word_replace = ['+'+str(i) for i in range(11)] + ['**1', '**2', '**3', '*-1', '']

    # 점수 3구간을 파악하기 위해서 숫자 앞에 해당하는 인덱스를 scor_index로 저장
    score_index = [index for index, w in enumerate(dartResult) if w in [str(i) for i in range(10)] + ['t']]

    # 그렇게 나눈 점수 계산이 필요한 3개 구간
    eval1, eval2, eval3 = dartResult[:score_index[1]], dartResult[score_index[1]:score_index[2]], dartResult[score_index[2]:]

    # 각 점수 세 구간의 가중치를 계산해서 가중합하는 방식을 쓰려고 함
    star = [index for index, w in enumerate(dartResult) if w == '*'] # '*'가 각 계산 구간에 영향을 미치므로 '*'가 위치한 인덱스 파악..
    star_index = [[], [2], [4], [5], [6], [7], [8], [2, 5], [2, 7], [2, 8], [4, 7], [5, 8], [2, 5, 8]]
    star_weight = [[1, 1, 1], [2, 1, 1], [2, 2, 1], [2, 2, 1], [1, 2, 2], [1, 2, 2], [1, 2, 2], [4, 2, 1], [2, 2, 2], [2, 2, 2], [2, 4, 2], [2, 4, 2],  [4, 4, 2]] # 노가다
    weight = star_weight[star_index.index(star)] # 주어진 dartResult에서 '*'의 인덱스 위치에 따른 각 계산 구간의 가중치를 weight로 저장

    # 세 구간을 각각 계산
    result1, result2, result3 = '', '', ''
    for index, w in enumerate(eval1):
        result1 += word_replace[word_list.index(w)]
    for index, w in enumerate(eval2):
        result2 += word_replace[word_list.index(w)]
    for index, w in enumerate(eval3):
        result3 += word_replace[word_list.index(w)]
    
    # 세 계산의 가중합 계산
    return eval(result1 * weight[0] + result2 * weight[1] + result3 * weight[2])