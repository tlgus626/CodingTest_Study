from collections import defaultdict
def solution(phone_book):
    a=defaultdict(int)
    for i in phone_book:
        a[i]
    for j in phone_book:
        b=''
        for k in j :
            b+=k
            if b in a and b != j :
                return False
    return True
