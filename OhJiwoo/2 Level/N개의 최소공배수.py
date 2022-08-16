import math
def solution(arr):
    while len(arr)>=2:
        a=arr.pop()
        b=arr.pop()
        gcd=math.gcd(a,b)
        lcm=(a//gcd)*(b//gcd)*gcd
        arr.append(lcm)
    return arr[0]
