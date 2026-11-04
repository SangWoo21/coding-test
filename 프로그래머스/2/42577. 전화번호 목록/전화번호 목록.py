# 아이디어: 번호를 set에 저장 → 각 번호의 앞부분(number[:i])이 set에 있으면 False
def solution(phone_book):
    nums = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in nums:
                return False
    return True