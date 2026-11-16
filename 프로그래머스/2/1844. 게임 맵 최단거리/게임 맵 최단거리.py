# 아이디어: 시작 칸(0,0)에서 BFS로 상하좌우 한 칸씩 퍼져 나가며 거리 기록 → 다음 칸 거리 = 지금 칸 거리 + 1 → BFS는 가까운 칸부터 처리하므로 "처음 도착한 거리 = 최단 거리" → 도착 칸(n-1, m-1)에 못 가면(거리 0) -1 반환
# DFS = 모든 경우의 수 / BFS = 최단 거리·최소 횟수
#
# [BFS 기본 틀]
# q = deque([시작]); 시작 방문 표시
# while q:
#     cur = q.popleft()
#     for 다음 in 인접한 곳(cur):
#         if 범위 안 and 갈 수 있음 and 아직 안 감:
#             방문 표시(다음)    ← 큐에 넣을 때 바로 표시 
#             q.append(다음)
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque([(0, 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist[n-1][m-1] if dist[n-1][m-1] else -1