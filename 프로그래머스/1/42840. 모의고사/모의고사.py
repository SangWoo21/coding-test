# 아이디어: 수포자 3명의 찍기 패턴을 리스트로 묶어 한 명씩 채점 → i번 문제에서 패턴 값은 p[i % len(p)] (패턴이 끝나면 처음부터 반복) → 최고점과 같은 사람을 모두 담아 반환 (1번부터 확인하므로 자동 오름차순)
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    score = [0, 0, 0]
    for i, a in enumerate(answers):     
        if a == p1[i % len(p1)]:
            score[0] += 1
        if a == p2[i % len(p2)]:
            score[1] += 1
        if a == p3[i % len(p3)]:
            score[2] += 1
    top = max(score)
    for n in range(3):        
        if score[n] == top:
            answer.append(n + 1) 
    return answer