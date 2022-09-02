def solution(p):
    
    new_str = ''
    left, right = 0, 0

    for i in p:

        if i == '(': left += 1
        else: right += 1

        new_str += i

        # 좌, 우 괄호 개수가 같을 때 비교
        if left == right:

            # 시작과 끝이 올바르면 pass
            if new_str[0] == '(' and new_str[-1] == ')':
                new_str = ''
                left, right = 0, 0
            
            # 시작 혹은 끝 중 하나라도 다르면 False
            else:
                new_str = ''
                left, right = 0, 0
                return False
    
    # 마지막에 대해서 좌, 우 괄호 개수가 다르면 False
    if left != right:
        return False

    return True