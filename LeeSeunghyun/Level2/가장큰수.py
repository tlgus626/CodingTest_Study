def solution(numbers):
    res = []
    
    for number in numbers: 
        prev = str(number)
        add= list(str(number))

        i = 0
        while len(add) < 4:
            add.append(prev[i])
            i = (i + 1) % len(prev)
        add = int("".join(add))
        res.append([add, prev])

    res = sorted(res, reverse = True)
    return str(int("".join(unit[1] for unit in res)))