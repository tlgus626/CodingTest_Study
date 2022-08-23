def solution(s):
    # length of zipped string <= len(s)
    MIN = len(s)

    # zip unit : 1 ~ len(s)//2
    for x in range(1, len(s) // 2 + 1):

        # split per unit
        stack = []
        for i in range(0, len(s), x):
            stack.append(s[i:i + x])

        # zip
        i, j = 0, 1
        nums = [0] * len(stack) # is ith number duplicated?
        while True:
            # if duplicated
            if i + j < len(stack) and stack[i] == stack[i + j]:
                nums[i] += 1
                j += 1
            # not duplicated
            else:
                nums[i] += 1
                i += j
                j = 1
            # until check all elements of stack
            if i == len(stack):
                break

        # make string
        res = ''
        for i in range(len(stack)):
            if nums[i] == 1:
                res += stack[i]
            elif nums[i] > 1:
                res += str(nums[i]) + stack[i]
        if len(res) < MIN:
            MIN = len(res)

    return MIN
