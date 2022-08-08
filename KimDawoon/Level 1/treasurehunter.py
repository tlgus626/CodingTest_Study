def solution(n, arr1, arr2):
    
    # dictionary 저장
    change = {'1':'#', '0':' '}
    
    # 각 숫자를 2진법 수로 받아드림
    ans = list(map(lambda x, y: str(format(x | y,'0'+str(n)+'b')),arr1,arr2))
    
    # dictionary를 이용해 1을 #으로 바꿈
    for i, j in zip(list(change.keys()),list(change.values())):
        ans = list(map(lambda x: x.replace(i,j),ans))
        
    return ans
