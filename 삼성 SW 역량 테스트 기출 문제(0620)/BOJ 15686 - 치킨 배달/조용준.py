from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []


for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            home.append((i,j))
        if town[i][j] == 2:
            chicken.append((i,j))

MIN = sys.maxsize
chicken_combi = list(combinations(chicken, m))

for case in chicken_combi:
    total = 0
    for i in range(len(home)):
        dist = sys.maxsize
        for x, y in case:
            dist = min(dist, abs(x-home[i][0])+abs(y-home[i][1]))
        total += dist
    MIN = min(MIN, total)
print(MIN)

# for i in range(len(home)):
#     total = 0
#     for case in chicken_combi:
#         dist = sys.maxsize
#         for x, y in case:
#             dist = min(dist, abs(x-home[i][0])+abs(y-home[i][1]))
#         total += dist
#     MIN = min(MIN, total)
# print(MIN)