def solution(record):

    act_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    # id: key, name: value 딕셔너리
    # Leave를 제외하고는 전부 3단어이고 Change는 가장 나중에 반영됨
    id_dict = {s.split()[1]: s.split()[2] for s in record if len(s.split()) == 3}

    result = []
    for s in record:

        # 'Change'가 들어간 구문은 패스
        if s.split()[0] == 'Change': pass

        # 딕셔너리 활용해서 새로운 출력 문장 저장
        else: result.append(id_dict[s.split()[1]] + act_dict[s.split()[0]])
    
    return result