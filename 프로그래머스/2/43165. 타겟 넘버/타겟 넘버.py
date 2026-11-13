# 아이디어: 숫자마다 +/-를 붙이는 모든 조합(2^n가지)을 DFS(재귀)로 끝까지 탐색
# DFS = 한 길을 끝까지 파고든 뒤 돌아와 다음 길을 탐색 (재귀/스택)
# BFS = 가까운 것부터 한 층씩 탐색 (큐), 최단 거리에 적합
# answer = 0 + nonlocal answer + answer += 1 방식으로 세도 결과 동일
def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        plus = dfs(idx + 1, total + numbers[idx])
        minus = dfs(idx + 1, total - numbers[idx])
        return plus + minus
    return dfs(0, 0)