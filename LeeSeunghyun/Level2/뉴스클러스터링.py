#결국엔 자카드 유사도 계산해라! 이것!!
#자카드 유사도란 결국 두 집합이 얼마나 비슷하냐에 대한 measure중 하나.
#기본 아이디어 : set들의 원소의 개수가 중요하다! "원소"가 아닌 "개수"로 접근

from collections import defaultdict
#defaultdict : 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 값을
#              디폴트 값으로(0) 지정하는 dictionary



def solution(str1, str2):

    
    str1,str2 = str1.lower(),str2.lower() #대소문자 구분 없으니, 소문자로 통일
    str1_dic,str2_dic = defaultdict(int),defaultdict(int) #딕셔너리 정의
    
    #set으로 접근하는게 아니라, dictionary로 접근. 어차피 겹치는 개수만 중요.
    #딕셔너리를 만들어 두 글자를 키로, 두 글자가 나온 횟수를 value에 저장
    
    #############################
    for i in range(len(str1)-1): #입력된 문자를 처음부터 싹 훑음.
        element = str1[i:i+2] #두 글자씩 끊어서 list(element)에다 저장
        if element.isalpha(): #문자열의 구성이 문자열인지 확인하는 방법(숫자, 공백, 특문 있으면 F)
            str1_dic[element]+=1 #똑같은 문자가 있으면, count횟수가 늘어남
    
    for i in range(len(str2)-1):#입력된 문자를 처음부터 싹 훑음.
        element = str2[i:i+2] #두 글자씩 끊어서 저장
        if element.isalpha(): #문자열의 구성이 문자열인지 확인하는 방법(숫자, 공백, 특문 있으면 F)
            str2_dic[element]+=1 #똑같은 문자가 있으면, count횟수가 늘어남
    #############################
    # -> 최종 dictionary형태는 각 두 글자가 key로, 해당 두 글자가 출현한 쵯수가 value로.
    
    
    #########교집합#################
    intersection = 0    
    for key,value in str1_dic.items():
        if str2_dic[key] is not None: #같은 key가 존재한다면
            intersection += min(value,str2_dic[key]) #dictionary를 탐색하면서, 
                                                     #intersection값을 취합.
    #자카드 유사도를 계산하는 거라서 이런 아이디어가 나옴
    #############################
    # -> 최종 dictionary형태는 각 두 글자가 key로, 해당 두 글자가 출현한 쵯수가 value로.

    
    ##########합집합################
    union = sum(list(map(lambda x:x[1],str1_dic.items()))) + #.items : 키, 밸류 모두
            sum(list(map(lambda x:x[1],str2_dic.items()))) - #value들만 다 빼와라
            intersection      
    #############################  
    
    
    
    if union == 0 :
        return 65536    
    
    return int(intersection/union * 65536) #자카드 유사도 기준에 따라


### 파이써닉한 모범답안 ### 

def solution(str1,str2):
    
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
    
    inter = sum([min(str1.count(word), str2.count(word)) for word in intersection])
    uni = sum([max(str1.count(word),str2.count(word)) for word in union])

    if uni ==0:
        return 65536
    return int(inter/uni * 65536)
