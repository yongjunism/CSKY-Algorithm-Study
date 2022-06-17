def solution(genres, plays):
    answer = []
    sum_play = {}
    rank = {}
    idx = 0
    
    for num, (genre, play) in enumerate(zip(genres, plays)):
        if genre in sum_play:
            sum_play[genre] += play
        else:
            sum_play[genre] = play
            
        if genre in rank:
            rank[genre].append((num, play))
        else:
            rank[genre] = [(num, play)]
        
    for genre, play in sorted(sum_play.items(), key=lambda item: item[1], reverse=True):
        idx = 0
        for num, play in sorted(rank[genre], key=lambda item: item[1], reverse=True):
            if idx == 2:
                break
            answer.append(num)
            idx += 1
    return answer