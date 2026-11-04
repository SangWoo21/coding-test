# 아이디어: set으로 중복 제거해 종류 수를 구함
def solution(nums):
    s = set(nums)
    if len(s) <= len(nums)/2:
        answer = len(s)
    else:
        answer = len(nums)/2
    return answer