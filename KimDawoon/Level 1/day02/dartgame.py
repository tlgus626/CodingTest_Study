def solution(dartResult):
    
    # dictionary definition
    dic = {'*':'', 'S#':'**1*(-1)+', 'D#':'**2*(-1)+', 'T#':'**3*(-1)+', 'S':'**1+', 'D':'**2+', 'T':'**3+'}
    numchange = {'10':'A'}
    
    # copy results
    s = dartResult
    s2 = dartResult
    
    # dictionary처럼 편하게 값 바꾸기
    for i, j in zip(list(dic.keys()),list(dic.values())):
        s = s.replace(i,j)
    
    # 세 번의 점수 계산하기
    s = s + '0'
    s1 = s.split('+')
    an = list(map(lambda x: eval(x),s1))
    
    # 숫자 10을 A로 바꿈
    for i, j in zip(list(numchange.keys()),list(numchange.values())):
        s2 = s2.replace(i,j)
    
    # '*'의 위치를 찾는것
    bol = [j+1 for i, j in zip(s2,range(len(s2))) if i == '*']

    # *의 위치를 기반으로 star점수 반영
    for i in bol:
        if i == 3:
            an[0] *= 2
        elif i in [5,6]:
            an[0] *= 2
            an[1] *= 2
        elif i in [7,8,9]:
            an[1] *= 2
            an[2] *= 2
        else:
            pass

    return sum(an)
