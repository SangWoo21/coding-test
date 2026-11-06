# 아이디어: 숫자를 문자열로 바꿔 "이어 붙였을 때 큰 순서"로 정렬 → join → 원소가 최대 1000(4자리)이라 x*3을 key로 내림차순 정렬
#문자열로 바꾸면 9가 10보다 크기 때문에 앞자리 기준 정렬에 적합
def solution(numbers):
    nums = [str(n) for n in numbers]
    nums.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(nums)
    return '0' if answer[0] == '0' else answer