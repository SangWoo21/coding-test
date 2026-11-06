#arr에서 for문으로 i번째랑 i-1번째가 같은지 보고 다르면 answer에 join으로 추가하면 어때
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i - 1] != arr[i]:
                answer.append(arr[i])
    return answer