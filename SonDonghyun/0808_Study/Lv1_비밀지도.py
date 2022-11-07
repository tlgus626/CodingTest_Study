def solution(n, arr1, arr2):
    
    # arr1과 arr2 내 원소에 bin 함수를 써서 이진법을 출력하되, 모든 숫자의 이진법 자릿수를 맞춰주기 위해 if문 사용
    bin_arr1 = [bin(num)[2:] if len(bin(num)[2:]) == n else '0' * (n - len(bin(num)[2:])) + bin(num)[2:] for num in arr1]
    bin_arr2 = [bin(num)[2:] if len(bin(num)[2:]) == n else '0' * (n - len(bin(num)[2:])) + bin(num)[2:] for num in arr2]
    
    # 리스트에 빈 문자열 원소 생성
    result = [''] * n

    # 반복문으로 공백 " " 혹은 "#" 채워넣기
    for i in range(n):
        for j in range(n): # 이중 반복문으로 시간복잡도 O(N^2)
            if bin_arr1[i][j] == '0' and bin_arr2[i][j] == '0': result[i] += " "
            else: result[i] += "#"
    
    return result