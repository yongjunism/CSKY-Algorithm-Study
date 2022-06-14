def solution(clothes):
    answer = 1
    dict_clothes = {}
    for i in clothes:
        if i[1] not in dict_clothes : dict_clothes[i[1]] = [i[0]]
        else: dict_clothes[i[1]].append(i[0])
        
    for key,value in dict_clothes.items():
        answer *= len(value)+1
    
    
    return answer-1