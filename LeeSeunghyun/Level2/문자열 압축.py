def solution(s):
    answer = len(s)
    
    ### 완전 탐색 ###
    
    ## step수 기준으로 outer 돌림 ###
    for step in range(1, len(s)+1):
        compressed = ''
        arr = []
        
        #arr이 비어있다면
        ## 해당 step수에 맞게 문자열 slice ##
        for start in range(0, len(s), step):
            end = start + step
            sliced = s[start:end]

            
            if start == 0:
               arr.append(sliced)
                
            else:
                if arr[-1] != sliced: # 중복 문자열을 체크하는 것이기 때문에 0이어도 무관
                    if len(arr) == 1:
                        compressed += f'{arr[-1]}'
                    else:
                        compressed += f'{len(arr)}{arr[-1]}'
                    arr = []
                
                arr.append(sliced)
        
        #arr이 비어있지 않다면
        if arr: 
            if len(arr) == 1:
                compressed += f'{arr[-1]}'
            else:
                compressed += f'{len(arr)}{arr[-1]}'
        
        
        answer = min([len(compressed), answer])
    
    return answer
