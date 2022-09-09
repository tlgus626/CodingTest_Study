def solution(w,h):
  #최대공약수 구하기
    def gcd(a,b): return b if (a==0) else gcd(b%a,a) 
  #(가로*세로)-(가로+세로-(가로, 세로의 최대공약수))  
    return (w*h)-(w+h-gcd(w,h))
