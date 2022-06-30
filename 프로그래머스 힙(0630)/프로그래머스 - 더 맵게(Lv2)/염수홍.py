import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    # 스코빌 배열을 힙큐로 만들어 줌, 최소가 앞으로
    cnt = 0
    while True:
        # 더 이상 더맵게 불가능
        _1 = heapq.heappop(scoville) # 첫번째 원소
        if _1 > K: # 다 맵게 완료
            return cnt
        if len(scoville) == 0:
            return -1
        _2 = heapq.heappop(scoville) # 두번째 원소
        heapq.heappush(scoville, _1 + _2 * 2)
        cnt += 1


    return cnt