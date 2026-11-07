#6 5 3 1 0 # 10 10 10
def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return answer
        else:
            answer += 1
    return answer