begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    stack = []
    stack.append(begin)
    visited = [ [0] for _ in range(len(words))]
    # visitied를 넣어줘야함

    def DFS():
        cnt = 0
        for i in range(len(words)):
            if stack:
                cur_word = list(stack.pop())
            if ''.join(cur_word) == target:
                return cnt
            temp_cnt = 0
            if cur_word[0]  == words[i][0]:
                temp_cnt += 1
            if cur_word[1] == words[i][1]:
                temp_cnt += 1
            if cur_word[2] == words[i][2]:
                temp_cnt += 1
            if temp_cnt == 2 :
                cnt += 1
                visited[i] = 1
                stack.append(words[i])
        return 0
    answer = DFS()
    return answer-1

solution(begin, target, words)