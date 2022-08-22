from collections import defaultdict
#defaultdict : 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 값을
#              디폴트 값으로(0) 지정하는 dictionary


def solution(str1, str2):

    
    str1,str2 = str1.lower(),str2.lower()
    str1_dic,str2_dic = defaultdict(int),defaultdict(int)
    
    #딕셔너리를 만들어 두 글자를 키로, 두 글자가 나온 횟수를 value에 저장
    #############################
    for i in range(len(str1)-1):
        element = str1[i:i+2] #두 글자씩 끊어서 저장
        if element.isalpha(): #문자열의 구성이 문자열인지 확인하는 방법(숫자, 공백있으면 F)
            str1_dic[element]+=1 #
    
    for i in range(len(str2)-1):
        element = str2[i:i+2] #두 글자씩 끊어서 저장
        if element.isalpha(): #문자열의 구성이 문자열인지 확인하는 방법(숫자, 공백있으면 F)
            str2_dic[element]+=1
    #############################
    
    
    #########교집합#################
    intersection = 0    
    for key,value in str1_dic.items():
        if str2_dic[key] is not None:
            intersection += min(value,str2_dic[key])
    #############################
    
    
    ##########합집합################
    union = sum(list(map(lambda x:x[1],str1_dic.items()))) + 
            sum(list(map(lambda x:x[1],str2_dic.items()))) -
            intersection      
    #############################  
    
    if union ==0:
        return 65536    
    
    return int(intersection/union * 65536)


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
