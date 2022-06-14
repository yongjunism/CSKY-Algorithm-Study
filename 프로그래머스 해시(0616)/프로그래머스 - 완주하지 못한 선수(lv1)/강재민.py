def solution(participant, completion):
    table = {}
    for i in completion :
        if i not in table :
            table[i] = 1
        else : table[i]+=1
    for j in participant :
        if j not in table :
            return j
        else :
            table[j] = table[j]-1
            if table[j]<0 :
                return j