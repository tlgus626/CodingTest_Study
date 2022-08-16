def solution(record):
    
    answer = []
    dic = {}

    # 유저 id 기준으로 저장 ex) { userid1 : 닉네임1 , userid2 : 닉네임2, ... }
    # leave의 경우 닉네임 변경과는 관련 없기 때문에, enter와 change의 경우만 다루기로 정함.
    # 유저 닉네임을 변경하면 자동으로 수정 되도록 코드 구성 
    # -> 어차피 시계열로 순차적으로 데이터가 구성되어있기 때문에, dictionary가 최종 수정된 완성된 결과를 나타냄

    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    #print

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % dic[sentence_split[1]])

    return (answer)