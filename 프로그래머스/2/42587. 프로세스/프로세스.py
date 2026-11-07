# 아이디어: 각 프로세스에 (우선순위, 원래 번호) 번호표를 붙여 deque에 넣음
# rotate(-1) = popleft() 후 append() (맨 앞 → 맨 뒤)
from collections import deque
def solution(priorities, location):
    q = deque((p, i) for i, p in enumerate(priorities))
    order = 0
    while q:
        if q[0][0] < max(p for p, i in q):  
            q.rotate(-1)
        else:
            p, i = q.popleft()                
            order += 1
            if i == location:
                return order