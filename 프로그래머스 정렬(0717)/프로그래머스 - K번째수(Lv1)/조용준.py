def solution(array, commands):
    answer = []
    for command in commands:
        start, end, idx = command[0] - 1, command[1], command[2] - 1
        answer.append(sorted(array[start:end])[idx])
    return answer