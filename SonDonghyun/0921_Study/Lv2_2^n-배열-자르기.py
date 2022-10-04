def solution(n, left, right):
    m1, n1 = divmod(left, n)
    m2, n2 = divmod(right, n)
    if m1 != m2:
        arr = [j + 1 if i <= j else i + 1 for j in range(m1 + 1, m2) for i in range(n)]
        left_arr = [m1 + 1 if i <= m1 else i + 1 for i in range(n) if i >= n1]
        right_arr = [m2 + 1 if i <= m2 else i + 1 for i in range(n) if i <= n2]
        result = left_arr + arr + right_arr
    else:
        result = [m1 + 1 if i <= m1 else i + 1 for i in range(n) if i >= n1 and i <= n2]

    return result
