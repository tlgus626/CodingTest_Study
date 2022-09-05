def solution(W, H):
    
    def gcd_lcm(a, b): # 유클리드 호제법
        p, q = max(a, b), min(a, b)
        while q:
            p, q = q, p % q
    
        return (p, a * b // p)
    
    gcd, lcm = gcd_lcm(W, H)
    y, x = max(W, H) // gcd, min(W, H) // gcd # y축의 변화량, x축의 변화량
    
    slice = lcm // x # 일단 무조건 잘려나가는 조각의 수
    num_rep = lcm // y # 예외적으로 잘려나가는 조각의 수를 찾기 위한 반복횟수 계산

    edit_slice = 0 # 예외적인 조각의 수
    
    # 나머지가 0이 아니면 예외적인 조각으로 카운트
    for i in range(1, num_rep + 1):
        if (y * i) % x != 0: edit_slice += 1
    
    return W * H - slice - edit_slice

