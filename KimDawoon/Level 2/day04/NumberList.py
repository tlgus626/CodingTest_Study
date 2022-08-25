def solution(phone_book):
    
    # hash dictionary
    hash = {k:1 for k in phone_book}
    
    # 해쉬를 이용한 비교
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            # 제 변수가 아닌 다른 곳에서 hash 반응이 나오면 False
            if temp in hash and temp != i:
                print(temp)
                return False
            
    return True

# 처음 의도했던 모범답안
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook[:-1], phoneBook[1:]):
        if p2.startswith(p1): # p2가 p1으로 시작하면 True
            return False
    return True
