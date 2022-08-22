def solution(phone_book):
    # len(x) : prefix string is always shorter than others.
    phone_book.sort(key=lambda x: (x, len(x)))
    # is jth string starts with ith string?
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
            break
    else:
        return True
