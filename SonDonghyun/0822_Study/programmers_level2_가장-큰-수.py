def solution(numbers):

    # 정렬 리스트를 짬
    num_len3 = [str(i) for i in range(999, 99, -1)]
    num_len2 = [str(i) for i in range(99, 9, -1)]
    num_len1 = [str(i) for i in range(9, 0, -1)]

    for i in num_len2:
        if i[0] > i[1]:
            num_len3.insert(num_len3.index(i + i[0]) + 1, i)
        else:
            num_len3.insert(num_len3.index(i + i[0]), i)

    for i in num_len1:
        num_len3.insert(num_len3.index(i + i) + 1, i)

    num_len3 = num_len3 + ['1000', '0']

    # 정렬 리스트 인덱스 순으로 정렬
    return str(int("".join(sorted([str(i) for i in numbers], key = num_len3.index))))