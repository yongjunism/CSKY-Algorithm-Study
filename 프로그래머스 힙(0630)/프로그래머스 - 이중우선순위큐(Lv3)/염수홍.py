# I 숫자 insert number / D 1 최댓값 삭제 최대힙 만들기(-붙여서 넣기) / D -1 최소값 삭제 heap[0]

import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:  # 배열 순회
        if operation[0] == 'I':  # insert
            heapq.heappush(min_heap, int(operation[2:]))
            # heapq.heappush(max_heap, -int(operation[2:]))
            pass
        elif operation[0] == 'D':
            if len(min_heap) > 0:
                if operation[2] == '-':  # 최소 삭제
                    heapq.heappop(min_heap)
                else:  # 최대 삭제
                    min_heap.remove(max(min_heap))

    if len(min_heap) > 0:
        return [max(min_heap), min(min_heap)]
    else:
        return [0, 0]