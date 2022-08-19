def solution(numbers):
    # 리스트 각 원소를 string으로 변경
    # string *3으로 길이를 3배 늘리고 값 비교
    # 순서를 다 구하면 크기가 큰 순으로 나열
    v = sorted(list(map(str,numbers)),key=lambda x: x*3,reverse=True)
    
    # str(int()) 랑 비교했을 때 소요시간이 더 짧음.
    return ''.join(v) if not all(c == "0" for c in v) else "0"
    #return str(int(''.join(v)))
