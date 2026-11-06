# 아이디어: '('면 +1, ')'면 -1 → cnt = 아직 짝이 없는 '('의 개수 (스택을 숫자로 대체) → 중간에 cnt < 0이면 ')'가 먼저 나온 것 → 즉시 False → 끝까지 갔을 때 cnt == 0이어야 True
def solution(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0