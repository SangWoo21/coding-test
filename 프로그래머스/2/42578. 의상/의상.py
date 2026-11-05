#아이디어: 종류별 개수를 딕셔너리로 셈 -> 종류마다 "안 입기"를 포함해 (개수 + 1)가지 선택해서 곱한 후 -1
def solution(clothes):
    cnt ={}
    for name, kind in clothes:
        cnt[kind] = cnt.get(kind, 0) + 1
        answer = 1
        for v in cnt.values():
            answer *= (v + 1)
    return answer - 1