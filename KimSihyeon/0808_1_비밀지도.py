def solution(n, arr1, arr2):

    # 이진수 만들어서 n자리 수로 맞춰주는 함수 생성
    def get2(x) :
        # 이진수 만들기
        res = []
        while True :
            res.append(x%2)
            x = x//2
            if x in [0,1] :
                res.append(x)
                break
        # n자리 수로 맞춰주기
        while len(res) < n :
            res.append(0)
        # 이진수는 거꾸로 뒤집어야 함
        return list(reversed(res))

    answer = []
    for i in range(n) :
        # 각 array의 i번째 행
        a1, a2 = arr1[i], arr2[i]
        # 각 array의 i번째 행에 get2 함수 적용
        n1, n2 = get2(a1), get2(a2)

        row = ''
        for j in range(n) :
            if n1[j] == 0 and n2[j] == 0 :
                row += ' '
            else :
                row += '#'
        answer.append(row)
        
    return answer