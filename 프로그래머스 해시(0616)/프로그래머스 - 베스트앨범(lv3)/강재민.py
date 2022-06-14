def solution(genres, plays):
    answer = []
    
    dict_album = {}
    #장르별 딕셔너리로 분류해주기
    for i in range(len(plays)):
        if genres[i] not in dict_album:
            dict_album[genres[i]] = {i:plays[i]}
        else:
            dict_album[genres[i]][i] = plays[i]
    
    #장르별 max value 2개씩만 남기기
    for genre in dict_album.keys():
        dict_album[genre] = sorted(dict_album[genre].items(),key = lambda x: (-x[1],x[0]))
    dict_album = sorted(dict_album.items(), key = lambda x: -sum(map(lambda y : y[1],x[1])))
    
    for jenre_key in dict_album:
        idx = 0
        for value in jenre_key[1]:
            if idx == 2: break
            answer.append(value[0])
            idx+=1
    return answer
