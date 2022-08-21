# key : 시작 번호가 같은 것들끼리 대소 비교하는 방식?

def solution(numbers) :
    answer = ''
    # 9로 시작하는 것들부터 붙여나가야 숫자가 가장 큼
    for i in range(9,0,-1) :
        nums = [str(x) for x in numbers if str(x)[0] == str(i)]
        res = ''
        # 만약 특정 번호로 시작하는 수들이 많은 경우 : ['1','104'] -> ['1111', '104104104']로 해놓고 대소 비교
        if len(nums) > 1 :
            nums.sort(key=lambda x : x*3, reverse=True)
            res = ''.join(nums)
        # 특정 번호로 시작하는 수가 하나인 경우
        elif len(nums) == 1 :
            res = nums[0]
        answer += str(res)
    # 0은 그냥 개수만큼 붙여주면 됨
    for _ in ['0' for x in numbers if x == 0] :
        answer += '0'
    # '000'이 정답인 경우를 고려하여, string으로 변환하기 전 int() 한번 해주기
    return str(int(answer))