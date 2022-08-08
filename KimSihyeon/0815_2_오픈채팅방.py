def solution(record):

    # 각 uid 별로 최종 닉네임 기록
    info = {}
    for r in record:
        if r.startswith('Leave') == False:
            _, uid, name = r.split()
            info[uid] = name

    # record 텍스트를 최종 닉네임으로 바꾸기
    answer = []
    for r in record:
        if r.startswith('Enter'):
            uid = r.split()[1]
            answer.append(info[uid] + '님이 들어왔습니다.')
        elif r.startswith('Leave'):
            uid = r.split()[1]
            answer.append(info[uid] + '님이 나갔습니다.')

    return answer