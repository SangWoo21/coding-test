# 아이디어: 컴퓨터 0번부터 차례로 보며, 아직 방문 안 한 컴퓨터를 만나면 새 네트워크 (answer += 1) → 그 컴퓨터에서 dfs로 연결된(computers[i][j] == 1) 컴퓨터를 모두 방문 표시 → 같은 네트워크의 나머지는 이미 visited라 다시 세지 않음
def solution(n, computers):
    visited = [False] * n
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
                
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer