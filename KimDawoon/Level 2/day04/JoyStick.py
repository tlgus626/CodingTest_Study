# 도저히 정답이 안나와서 정답자거 참조해서 풀었음
def solution(name):
    
    # 상하 횟수 세기
    k = [min(ord('Z')-ord(i)+1,ord(i)-ord('A')) for i in name]
    cnt = sum(k)
    
    # 좌우 횟수 세기
    # 좌 또는 우로 변동없이 계속 움직이는 횟수 저장
    move = len(name) - 1
    
    # 길이만큼 움직임
    for idx in range(len(name)):
        # 오른쪽 항목 확인
        next_idx = idx + 1
        
        # 오른쪽 옆 글자가 마지막 글자가 아니면서, 'A'인 경우 다음 인덱스로
        while (next_idx < len(name)) and (name[next_idx] == 'A'):
            next_idx += 1
        
        # 두 인덱스 사이의 값이 1이면 다음으로 패스
        # 어차피 최소가 안될 가능성이 높다.
        if next_idx - idx == 1:
            continue
        
        # 첨부 참조
        distance = min(idx, len(name) - next_idx)
        move = min(move, idx + len(name) - next_idx + distance)
    
    # 상하 + 좌우
    return cnt + move
