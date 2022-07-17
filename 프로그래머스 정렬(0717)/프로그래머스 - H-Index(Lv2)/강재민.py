def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    answer = max(map(min, enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))
    return answer