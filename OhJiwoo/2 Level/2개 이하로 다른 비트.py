def solution(numbers):
    answer = []
    for  i in numbers:
        bit=(i ^ i+1) >> 2 
        answer.append(i+1+bit)
    return answer
