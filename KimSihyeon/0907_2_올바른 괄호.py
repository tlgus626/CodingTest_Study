def solution(s):
    stack = []
    for x in s:
        # 열린 괄호는 append
        if x == '(':
            stack.append(x)
        else:
            # 닫힌 괄호가 나오면 열린 괄호를 pop -> 한 세트니까!
            if len(stack) > 0:
                stack.pop()
            # stack이 비어있는데 닫힌 괄호가 들어오면 잘못된 배열 : False
            else:
                return False
    # stack이 비어있음 i.e., 모든 괄호들이 세트로 올바르게 존재함
    if len(stack) == 0:
        return True
    # stack이 비어있지 않음 i.e., 열린 괄호가 pop되지 못하고 남아있음
    else:
        return False
