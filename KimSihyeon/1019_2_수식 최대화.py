from itertools import permutations

# 사칙연산 수행하는 함수
def calculate(x, y, o):
    if o == '*':
        return x * y
    elif o == '+':
        return x + y
    else:
        return x - y

# 지정된 하나의 연산자를 이용해 계산
def get_result(stack, o):
    res = []
    k = -1
    for i in range(len(stack)):
        if i == k:
            pass
        else:
            if stack[i] != o:
                res.append(stack[i])
            else:
                res.append(calculate(res.pop(), stack[i + 1], o))
                k = i + 1
    return res


def solution(expression):
    exp_list = []
    operator = set()
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        # 연산자가 나오는 순간 tmp를 하나의 숫자로 바꿔줌
        else:
            exp_list.append(int(tmp))
            exp_list.append(e)
            operator.add(e)
            tmp = ''
    exp_list.append(int(tmp))

    # 연산자의 우선순위 리스트
    operator = list(permutations(operator))

    MAX = 0
    for o in operator:
        # 첫번째 우선순위 연산자로 계산한 결과를 stack에 담음
        stack = get_result(exp_list, o[0])
        # recurrently get_result(stack)
        for i in range(1, len(o)):
            stack = get_result(stack, o[i])
        # 최종 계산 결과가 최댓값인지?
        if abs(stack[0]) > MAX:
            MAX = abs(stack[0])

    return MAX