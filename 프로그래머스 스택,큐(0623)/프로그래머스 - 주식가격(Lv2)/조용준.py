def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        if i == len(prices)-1:
            answer.append(0)
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                answer.append(cnt)
                break
            if j == len(prices)-1:
                answer.append(cnt)
    return answer