# 아이디어: 전체 넓이 total = brown + yellow = w * h → h를 3부터 하나씩 대입 (노란색이 최소 1칸이라 h - 2 >= 1) → total이 h로 나누어떨어지면 w = total // h → w >= h이고 (w - 2) * (h - 2) == yellow이면 정답
def solution(brown, yellow):
    total = brown + yellow
    for h in range(3, total + 1):
        if total % h == 0:
            w = total // h
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w, h]