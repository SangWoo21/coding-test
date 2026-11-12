# 아이디어: 정렬 후 가장 가벼운 사람(left)과 가장 무거운 사람(right)을 짝지음
# 투 포인터 : 양 끝에서 안쪽으로 좁혀 오며 탐색 (left > right면 종료)
def solution(people, limit):
    people.sort()                    
    left = 0                       
    right = len(people) - 1         
    boat = 0

    while left <= right:             
        if people[left] + people[right] <= limit:  
            left += 1              
        right -= 1                 
        boat += 1             
    return boat