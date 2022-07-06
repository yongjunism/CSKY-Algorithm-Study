def solution(phone_book):
    setPhonebook = set(phone_book)
    for Phonenumber in setPhonebook:
        for i in range(1, len(Phonenumber)):
            if Phonenumber[:i] in setPhonebook:
                return False
    return True