# 아이디어: 이름별 개수를 딕셔너리로 +1/-1 → 값이 남은 이름이 정답
def solution(participant, completion):
    cnt = {}
    for name in participant:
        cnt[name] = cnt.get(name, 0) + 1
    for name in completion:
        cnt[name] -= 1
    for name, v in cnt.items():
        if v > 0:
            return name