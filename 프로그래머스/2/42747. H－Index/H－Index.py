# 아이디어: 인용 횟수를 내림차순 정렬 → 앞에서부터 (i+1)번째 논문이 i+1회 이상 인용됐는지 확인하며 개수를 셈
# sort(reverse=True) = 내림차순 정렬 / reverse() = 순서만 뒤집기
def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return answer
        else:
            answer += 1
    return answer