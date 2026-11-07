# 아이디어: 기능마다 남은 일수 d = ceil((100 - 진도) / 속도) 계산
# answer[-1] += 1 → 리스트 마지막 값을 직접 수정
import math
def solution(progresses, speeds):
    answer = []
    cur = 0                                     
    for p, s in zip(progresses, speeds):
        d = math.ceil((100 - p) / s)              
        if d > cur:                              
            cur = d
            answer.append(1)
        else:                                     
            answer[-1] += 1
    return answer