from itertools import permutations

def solution(numbers):
    answer = ''
    num_list = []
    perms = list(permutations(numbers, len(numbers)))
    for perm in perms:
        num = ''
        for element in perm:
            num += str(element)
            num_list.append(int(num))
    num_list.sort(reverse=True)
    answer = str(num_list[0])
    return answer