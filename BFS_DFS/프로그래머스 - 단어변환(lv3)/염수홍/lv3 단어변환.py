begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]



def solution(begin, target, words):
    stack = []
    stack.append(begin)
    def DFS():
        cnt = 0
        for word in words:
            if stack:
                cur_word = list(stack.pop())
            if ''.join(cur_word) == target:
                return cnt
            temp_cnt = 0
            if cur_word[0]  == word[0]:
                temp_cnt += 1
            if cur_word[1] == word[1]:
                temp_cnt += 1
            if cur_word[2] == word[2]:
                temp_cnt += 1
            if temp_cnt > 1:
                cnt += 1
                stack.append(word)
        return cnt
    answer = DFS()
    print(answer)
    return answer


solution(begin, target, words)