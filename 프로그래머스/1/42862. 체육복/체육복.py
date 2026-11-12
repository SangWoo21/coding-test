# 아이디어: 체육복이 없는 학생을 번호 순서대로 보며 "앞번호 여벌부터" 빌림
# set : 중복을 없애거나 종류 수 셀 때, 값이 있는지 많이 확인할 때, 두 그룹의 교집합이나 차집합 구할 때 사용
def solution(n, lost, reserve):
    real_lost = sorted(set(lost) - set(reserve))     # 진짜 없는 학생
    real_reserve = set(reserve) - set(lost)          # 진짜 빌려줄 수 있는 학생

    for i in real_lost:
        if i - 1 in real_reserve:       
            real_reserve.remove(i - 1)
        elif i + 1 in real_reserve:      
            real_reserve.remove(i + 1)
        else:
            n -= 1                       
    return n