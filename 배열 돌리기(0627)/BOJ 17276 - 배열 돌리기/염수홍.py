import sys
sys.stdin = open('input1.txt')

T = int(input())
n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]