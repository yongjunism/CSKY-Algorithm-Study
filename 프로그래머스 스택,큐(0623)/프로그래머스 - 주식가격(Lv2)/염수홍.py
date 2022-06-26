

def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N): # prices 배열을 돌려줌
        cnt = 0
        for j in range(i + 1, N): # 나 다음거 뒤로 쭉 돌려줌
            if prices[i] > prices[j]: # 가격 하락시 break
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer



def solution2(prices):
    answer = []
    while prices:
        cnt = 0
        for j in range(1, len(prices)):
            if prices[0] > prices[j]:
                print(prices[0], prices[j])
                cnt += 1
                prices.pop(0)
                break
            else:
                cnt += 1
        answer.append(cnt)
        break
    return answer


def solution3(prices):
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