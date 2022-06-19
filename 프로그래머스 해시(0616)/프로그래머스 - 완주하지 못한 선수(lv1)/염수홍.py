
participant = ["marina", "marina", "nikola", "vinko", "filipa"]
completion = ["marina", "filipa", "marina", "nikola"]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

solution(participant, completion)

