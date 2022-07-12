def solution(citations):
    answer = 0
    MAX = max(citations)
    h_idx= [0] * (MAX+1)   
    for h in range(MAX+1):
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1
        h_idx[h] = cnt
    for idx, cnt in enumerate(h_idx):
        if cnt >= idx:
            answer = idx
    return answer