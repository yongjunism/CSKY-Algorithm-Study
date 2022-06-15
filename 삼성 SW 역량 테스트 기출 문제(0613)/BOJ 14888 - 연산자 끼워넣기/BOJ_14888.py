import sys
input = sys.stdin.readline

n = int(input())
operand = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

MAX, MIN = -1e9, 1e9

def dfs(idx, ans):
    global add, sub, mul, div, MAX, MIN
    if idx == n:
        MAX = max(MAX, ans)
        MIN = min(MIN, ans)
        return
    else:
        if add:
            add -= 1
            dfs(idx+1, ans + operand[idx])
            add += 1
        if sub:
            sub -= 1
            dfs(idx+1, ans - operand[idx])
            sub += 1
        if mul:
            mul -= 1
            dfs(idx+1, ans * operand[idx])
            mul += 1
        if div:
            div -= 1
            dfs(idx+1, int(ans / operand[idx]))
            div += 1

dfs(1, operand[0])
print(MAX)
print(MIN)