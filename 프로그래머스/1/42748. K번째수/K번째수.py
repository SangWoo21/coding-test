# 아이디어: 명령마다 array[i-1:j]로 자르고 정렬 → k-1번째 값을 answer에 추가
# 주의 : .sort()는 None을 반환 → 정렬된 값이 필요하면 sorted() 사용
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer

#for n in range(len(commands): i = commands[n][1]