import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

total = n

for num in a:
    num -= b
    if num > 0:
        if num % c:
            total += num // c + 1
        else:
            total += num // c

print(total)