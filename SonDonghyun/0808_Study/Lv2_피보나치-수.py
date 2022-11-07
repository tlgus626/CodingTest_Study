from collections import deque

def solution(n):
    
    F = deque([0, 1])

    for _ in range(n - 1):
        F.append(F[0] + F[1])
        F.popleft()
    
    return list(F)[1] % 1234567