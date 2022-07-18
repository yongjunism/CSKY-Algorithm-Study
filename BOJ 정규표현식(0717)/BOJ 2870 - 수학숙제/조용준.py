import sys, re
input = sys.stdin.readline

n = int(input())
strings = [input().rstrip() for _ in range(n)]
nums = []

for string in strings:
    num_list = re.findall('\d+', string)
    num_list = list(map(int, num_list))
    nums.extend(num_list)

nums.sort()

for num in nums:
    print(num)