from collections import defaultdict

def solution(str1, str2):

    
    str1,str2=str1.lower(),str2.lower()
    str1_dic,str2_dic = defaultdict(int),defaultdict(int)
    
    for i in range(len(str1)-1):
        element = str1[i:i+2]
        if element.isalpha():
            str1_dic[element]+=1
    
    for i in range(len(str2)-1):
        element = str2[i:i+2]
        if element.isalpha():
            str2_dic[element]+=1
    
    intersection = 0    
    for key,value in str1_dic.items():
        if str2_dic[key] is not None:
            intersection += min(value,str2_dic[key])
    union = sum(list(map(lambda x:x[1],str1_dic.items())))+sum(list(map(lambda x:x[1],str2_dic.items())))-intersection      
    if union ==0:
        return 65536    
    
    return int(intersection/union * 65536)