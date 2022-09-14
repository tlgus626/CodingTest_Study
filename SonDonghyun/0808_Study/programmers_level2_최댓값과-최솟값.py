def solution(s):
    answer = str(min(list(map(int, s.split())))) + " " + str(max(list(map(int, s.split()))))
    return answer