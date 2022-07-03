import heapq
import sys
sys.stdin = open('input1.txt')

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0: # 빈배열일경우
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else: # arr not empty
        heapq.heappush(arr, (abs(x), x))
