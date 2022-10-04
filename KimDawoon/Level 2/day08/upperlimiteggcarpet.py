def solution(brown, yellow):
    
    # yellow 타일 개수를 고정시키고 될 수 있는 모든 조합을 만든다.
    a = [[yellow//c+2,c+2] for c in range(1,int(yellow**0.5)+1) if yellow % c ==0]
    
    # 실제 brown타일 개수와 가상으로 만든 카펫타일의 개수와 같은것을 뽑아냄
    x = [a[i] for i in range(len(a)) if a[i][0]*a[i][1] - yellow == brown]
    
    # 가로 길이가 더 길기 때문에 더 먼저 나오는 값 출력
    return x[0]
