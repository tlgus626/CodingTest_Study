# 절대값 함수 정의
abs = lambda n: -n if n < 0  else n

# 하나의 부호만 계산해주는 함수 정의
def cal_exp(s, new_exp):

    new_cal = []
    pass_index = -1 # 이미 부호 뒤에 붙어서 계산된 숫자에 해당하는 인덱스 무시하기 위해 도입

    for i in range(len(new_exp)):

        if pass_index == i:
            pass_index = -1

        else:
            if new_exp[i] != s:
                new_cal.append(new_exp[i])
            else:
                a = new_cal.pop()
                if s == '*':
                    cal = a * new_exp[i + 1]
                elif s == '-':
                    cal = a - new_exp[i + 1]
                else:
                    cal = a + new_exp[i + 1]
            
                pass_index = i + 1
                new_cal.append(int(cal))
    
    return new_cal

def solution(expression):

    max_value = 0
    
    # 주어진 표현식을 리스트에 숫자와 부호 단위로 풀어서 저장할 것
    new_exp = []
    temp = ''
    for w in expression:

        if w.isdigit():
            temp += w
        else: # 부호가 나오면 temp로 저장한 숫자를 append하고 그다음 부호도 append
            new_exp.append(int(temp))
            new_exp.append(w)
            temp = '' # 초기화
    
    new_exp.append(int(temp)) # 저장되지 않은 마지막 숫자도 append
    
    # 6가지 부호 우선순위를 permutation 함수로 전부 적용하여 max값 찾음
    from itertools import permutations
    for i in permutations(['*', '-', '+'], 3):
        max_value = max(max_value, abs(cal_exp(i[0], cal_exp(i[1], cal_exp(i[2], new_exp)))[0]))

    return max_value