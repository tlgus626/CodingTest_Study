def solution(n, k):
    s=''
    while n:

        s += str(n % k)       # 나머지로 k진수 만들기
        n //= k

    s = s[::-1]
    
    def prime_num_check(p,i=2):   # 소수인지 확인
        num = int(p)

        if num==i:
            return True

        while True:
            r = num % i

            if r !=0:
                if i >num**0.5:   #제곱근으로 확인하여 시간복잡도 줄이기
                    return True
                i+=1
            else:
                return False    # 나머지가 0이 나오는 순간 반복문 stop
    answer = 0
    for p in s.split('0'):

        if p=='' or p=='1':    
            continue


        if prime_num_check(p)==True:
            answer+=1
    return answer
