import sys
sys.stdin = open('input1.txt')

sangdam = []
N = int(input())
for i in range(N):
    sangdam.append(list(map(int, input().split())))

print(sangdam)