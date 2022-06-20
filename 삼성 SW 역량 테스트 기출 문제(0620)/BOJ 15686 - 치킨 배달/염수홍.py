import sys 
sys.stdin = open('input1.txt')
from itertools import combinations

# 거리의 최소 값을 찾아서 result에 저장하는 ㅎ마수
result = []
def Findmin(house_points, chiken_points):
    global result
    min_distance = 0
    for house_point in house_points:
        min_num = N*2
        for chinken_point in chiken_points:
            distance = abs(abs(chinken_point[0] - house_point[0]) + abs(chinken_point[1] - house_point[1]))
            if distance < min_num: # 가장 작은 값으로 갱신
                min_num = distance
        min_distance += min_num
    result.append(min_distance)

# 기본 입력
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house_points, chicken_points = [],[]
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N): # 데이터를 받아오면서 치킨집과 집의 좌표를 동시에 찍어줌
        if city[i][j] == 1:
            house_points.append([i, j])
        elif city[i][j] == 2:
            chicken_points.append([i, j])

# 조합을 찾아서 돌려줌
Combis = list(combinations(chicken_points, M))
for Combi in Combis:
    Findmin(house_points, Combi)
print(min(result))
