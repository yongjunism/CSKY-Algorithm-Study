from collections import deque

def solution(begin, target, words):
    queue = deque([[begin,0]])
    visited = [0] * len(words)
    while queue:
        tmp = queue.popleft()
        if tmp[0] == target: 
            return tmp[1]
        for i in words:
            match = list(map(lambda x,y: x==y,tmp[0],i))
            if sum(match) == len(tmp[0])-1 and visited[words.index(i)] == 0:
                visited[words.index(i)] = 1
                queue.append([i,tmp[1]+1])
    return 0
                

    