import sys
input = sys.stdin.readline

n = int(input())
time = []
profit = []

dp = [0 for _ in range(n+1)]

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

for day in range(n):
    if day + time[day] <= n:
        dp[day + time[day]] = max(dp[day + time[day]], dp[day] + profit[day])
    dp[day+1] = max(dp[day+1], dp[day])
print(dp[n])