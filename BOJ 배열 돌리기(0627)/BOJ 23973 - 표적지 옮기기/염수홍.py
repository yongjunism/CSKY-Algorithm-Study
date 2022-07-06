import sys
sys.stdin = open('input1.txt')

N, M = map(int, input().split())
sqaure = [list(map(int, input().split())) for _ in range(N)]