from collections import deque


def solution(priorities, location):
    dq = deque()
    # make indices (in case of same name documents)
    for i, p in enumerate(priorities):
        dq.append((i, p))

    answer = 0
    while dq:
        p0 = dq.popleft()
        # first document's priority is highest
        if all(p0[1] >= p[1] for p in dq):
            answer += 1
            # first document is our target document
            if p0[0] == location:
                break
        # put it at last
        else:
            dq.append(p0)
    return answer
