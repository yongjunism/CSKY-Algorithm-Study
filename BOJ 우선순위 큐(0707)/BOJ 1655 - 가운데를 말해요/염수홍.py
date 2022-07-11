import sys
import heapq
sys.stdin = open('input1.txt')

input = sys.stdin.readline
N = int(input())

a_heap = []
b_heap = []
for i in range(N):
    a = int(input())
    if len(a_heap) == len(b_heap):
        heapq.heappush(a_heap, -a)
    else:
        heapq.heappush(b_heap, a)
    # print(a_heap, b_heap)

    if len(a_heap) > len(b_heap):
        print(-a_heap[0])
    else: # 같으면
        print(min(-a_heap[0], b_heap[0]))