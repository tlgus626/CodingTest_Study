def solution(s):

    if len(s) % 2 != 0: return 0

    renew = ['']
    for i in s:
        if i != renew[-1]:
            renew.append(i)
        else:
            renew.pop()
    
    return 1 if renew == [''] else 0