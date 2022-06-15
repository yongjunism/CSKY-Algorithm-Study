def solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    
    for i in phone_book:
        for j in range(len(i)):
            if i[:j] in hash_map and i[:j] != i:
                return False
    return True