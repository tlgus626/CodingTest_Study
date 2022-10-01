def solution(s):
    stack = []
    # initialize
    stack.append(s[0])
    # stack
    for x in s[1:]:
        if len(stack) > 0 and x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if len(stack) > 0:
        return 0
    else:
        return 1
