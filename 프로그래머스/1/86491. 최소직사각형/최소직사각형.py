# 아이디어: 명함마다 긴 쪽은 가로, 짧은 쪽은 세로로 돌려 놓음
def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        a = max(w, h)
        b = min(w, h)
        max_w = max(max_w, a)
        max_h = max(max_h, b)
    answer = max_w * max_h
    return answer