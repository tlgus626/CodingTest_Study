def solution(record):
    
    # 메세지 세 개의 단어로 분리
    message = list(map(lambda x: x.split(' '),record))
    
    # 최종 닉네임을 위한 dictionary 생성
    user = {c[1]:c[2] for c in message if c[0] != "Leave"}
    
    # 메세지 저장하기
    alarm = []
    for i in message:
        # Enter일 경우 dictionary를 이용해 저장된 닉네임을 출력
        if i[0] == 'Enter':
            alarm += [user[i[1]]+"님이 들어왔습니다."]
        
        # Leave일 경우 dictionary를 이용해 저장된 닉네임을 출력
        elif i[0] == 'Leave':
            alarm += [user[i[1]]+"님이 나갔습니다."]
            
        # Change는 안내 메시지가 없음
        else:
            pass
    
    return alarm
