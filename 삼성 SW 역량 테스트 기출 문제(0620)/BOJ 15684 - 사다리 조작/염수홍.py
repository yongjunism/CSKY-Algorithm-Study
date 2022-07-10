import sys
sys.stdin = open('input1.txt')
N, M, H = map(int, input().split()) # 세로선의 개수, 가로선의 개수, 가로선을 놓을 수 있는 위치의 개수
ladders = []

a, b = [list(map(int, input().split())) for _ in range(M)] # a번 가로 위치, b&b+1의 세로선을 연결함