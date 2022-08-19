def solution(n):
    
    def onetwofour(n):
        # divmod로 n-1의 몫과 나머지를 구함
        p,q = divmod(n-1,3)
        
        # 나머지의 숫자가 012지만 이것을 124로 바꾸면 치환 가능
        return onetwofour(p) + "124"[q] if p else "124"[q]
    
    #재귀함수 마무리
    return onetwofour(n)
