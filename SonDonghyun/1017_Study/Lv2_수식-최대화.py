abs = lambda n: -n if n < 0  else n

def cal_exp(s, new_exp):

    new_cal = []
    pass_index = -1

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
    new_exp = []
    temp = ''
    for w in expression:

        if w.isdigit():
            temp += w
        else:
            new_exp.append(int(temp))
            new_exp.append(w)
            temp = ''
    
    new_exp.append(int(temp))
    
    from itertools import permutations
    for i in permutations(['*', '-', '+'], 3):
        max_value = max(max_value, abs(cal_exp(i[0], cal_exp(i[1], cal_exp(i[2], new_exp)))[0]))

    return max_value