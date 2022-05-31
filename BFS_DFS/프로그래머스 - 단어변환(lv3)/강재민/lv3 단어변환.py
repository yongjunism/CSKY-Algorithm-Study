## 단어 간 다른 글자의 개수가 1개인것을 찾는 법이 핵심

from collections import deque

def solution(begin, target, words):
    queue = deque([[begin,0]]) #begin이 "hit"이고 인덱스를 0번으로 준다!
    visited = [0] * len(words) #이미 방문한 단어인지 확인해주는 리스트도 만들어준다.
    while queue: #현재는 ["hit",0] 들어있는 상태
        tmp = queue.popleft()
        if tmp[0] == target: #tmp[0] : "hit", target : "cog" 
            return tmp[1] #만일 같다면 더이상 while문 진행하지 않고 바로 탈출!
        for i in words: # words : ["hot","dot","dog","lot","log","cog"] 모두 한바퀴 돌아줍니다
            match = list(map(lambda x,y: x==y,tmp[0],i)) #x는 tmp[0] 즉 "hit"를 iter, y는 i즉 word리스트 중 한개를 iter해줍니다. 만일 char가 같다면 True , 1이 나오고 틀리다면 False , 0 반환
            if sum(match) == len(tmp[0])-1 and visited[words.index(i)] == 0: #만일 1개만 틀리고 나머지가 같다면 sum(match) == len(tmp[0]) -1이 성립합니다. 그리고 그 단어를 방문한 적이 없다면
                visited[words.index(i)] = 1 #방문처리를 완료해주고,
                queue.append([i,tmp[1]+1]) # 한글자만 차이나기 때문에 덱에 넣어줄 수 있습니다.
    return 0
                

    