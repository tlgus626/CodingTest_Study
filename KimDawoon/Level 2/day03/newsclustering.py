def solution(str1, str2):
    
    # 두 글자씩 따로 뽑아내는 list 만들어내기
    def list2set(st):
        # 대문자를 전부 소문자로 변경
        st = st.lower()
        # 문자열을 리스트로 치환
        lst = list(st)
        # 맨 앞글자부터 두번씩 출력하도록 만든 문자열
        k = ''.join(list(map(lambda x, y: x+y, lst,lst)))
        # 두글자씩 리스트로 출력하는 대신 두 글자 모두 알파벳일 경우만 출력
        split_data = [k for k in list(map(''.join, zip(*[iter(k[1:-1])]*2))) if k.isalpha()]
        return split_data
    
    # 두 string 전부 원소가 없으면 리턴
    if len(list2set(str2)) == 0 & len(list2set(str1)) == 0:
        return 65536
    
    # 교집합의 개수를 카운팅
    o = list2set(str2)
    k = 0
    for i in list2set(str1):
        if i in o:
            k += 1
            # 중복 원소 개수 맞추기 위한 원소 제거
            o.pop(o.index(i))
            
    # AUB = A+B-AB
    return int(k/(len(list2set(str2))+len(list2set(str1))-k)*65536)
