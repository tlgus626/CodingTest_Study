def solution(s):

    # 문자열 압축 함수 정의
    def comp_string(s):
        temp = '' # 바로 이전에 확인한 문자 temp에 저장
        cnt = 0
        result = ''

        for c in s:
            if c != temp: # 지금 문자가 temp랑 같으면 (즉, 반복이 아니면)
                if cnt > 1: result += str(cnt) + temp
                elif cnt == 1: result += temp
                temp = c # 반복이 끝났으므로 temp를 지금 보는 문자로 변경
                cnt = 1 # 카운트 1로 초기화
            
            else: cnt += 1 # 반복이면 반복 카운트

        # 마지막 문자도 확인하고자 추가
        if cnt > 1: result += str(cnt) + temp
        elif cnt == 1: result += temp
        
        return result
    
    # 문자열 길이가 1인 경우 1 리턴
    if len(comp_string(s)) == 1:
        return 1
    
    # 문자열 길이가 1이 아닌 경우
    else:
        len_list = []

        # 문자열을 1칸부터 문자열 길이의 절반까지 잘라서 comp_string 함수 적용
        for l in range(1, int(len(s) / 2) + 1):
            a = [s[i:i + l] for i in range(0, len(s), l)]
            len_list.append(len(comp_string(a)))
    
    return min(len_list)
