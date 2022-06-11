import sys
sys.stdin = open('input3.txt')
from itertools import combinations
# 모인사람 N명 짝수, N/2 스타트팀, 링크팀
# a, b 사람이 같은팀되면 powers[a][b] + powers[b][a] 의 능력치임
# 능력치의 차이를 최소로
# 20명의 조합을 짜야함

input = sys.stdin.readline
N = int(input())
all_member = [i for i in range(1, N+1)]
powers = [list(map(int, input().split())) for _ in range(N)]
teams = list(combinations(range(1,N+1), int(N/2)))
min_num = float('inf')
visited = []

for start_team in teams:
    start_power, link_power = 0, 0
    link_team = list(set(all_member) - set(start_team))# 차집합으로 link팀의 멤보를 구해줌
    for member in start_team:
        for num in range(1, N+1):
            if num in start_team and num != member:
                start_power += powers[member-1][num-1]
            elif num in link_team and num != member:
                link_power += powers[member - 1][num - 1]

    if min_num > abs(start_power - link_power):
        min_num = abs(start_power - link_power)

print(min_num)



