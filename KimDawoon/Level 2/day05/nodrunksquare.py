def solution(w,h):
    
    # 최대공약수 찾는 식
    def gcd(w, h):
        return w if h == 0 else gcd(h, w % h)
    
    # 전체 - 행 - 열 + 최대공약수
    return w*h -w -h +gcd(w,h)
