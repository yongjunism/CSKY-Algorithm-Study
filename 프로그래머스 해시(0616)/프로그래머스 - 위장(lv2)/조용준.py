def solution(clothes):
    answer = 1
    clothes_dict = {}
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind].append(name)
        else:
            clothes_dict[kind] = [name]
    for kind in clothes_dict.keys():
        answer *= len(clothes_dict[kind]) + 1
    return answer - 1