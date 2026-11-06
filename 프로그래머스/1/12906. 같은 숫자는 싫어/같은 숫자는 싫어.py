# 아이디어: 인덱스로 돌면서 바로 앞 원소(arr[i-1])와 다를 때만 answer에 append → 첫 원소(i == 0)는 비교 대상이 없으므로 무조건 추가
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i - 1] != arr[i]:
                answer.append(arr[i])
    return answer