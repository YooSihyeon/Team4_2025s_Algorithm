import sys
sys.setrecursionlimit(10000)  # 깊은 재귀 호출이 가능하도록 제한 증가

# 8방향 이동 정의 (상, 하, 좌, 우, 그리고 대각선 4방향)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

# DFS 함수 정의: 현재 위치 (x, y)에서 출발하여 0을 찾는지 탐색
def dfs(grid, visited, path, x, y):
    n = len(grid)  # 격자 크기

    # 현재 좌표가 범위 밖이면 False
    if not (0 <= x < n and 0 <= y < n):
        return False

    # 이미 방문했거나 장애물(음수 포함)이라면 탐색 종료
    if visited[x][y] or grid[x][y] < 0:
        return False

    # 현재 위치를 경로에 추가하고 방문 처리
    path.append((x, y))
    visited[x][y] = True

    # 0이라면 도착 성공
    if grid[x][y] == 0:
        return True

    # 현재 칸의 숫자만큼 점프해서 8방향 탐색
    jump = grid[x][y]
    for dx, dy in directions:
        nx, ny = x + dx * jump, y + dy * jump
        if dfs(grid, visited, path, nx, ny):  # 재귀적으로 이동
            return True

    # 여기는 막다른 길 → 경로에서 제거 (백트래킹)
    path.pop()
    return False

n = int(input())
# 격자 내용 입력 (한 줄씩 정수 리스트로 받음)
grid = [list(map(int, input().split())) for _ in range(n)]
# 방문 기록 저장용 2차원 리스트
visited = [[False]*n for _ in range(n)]
# 경로를 저장할 리스트
path = []
# (0, 0)에서 시작하여 DFS 수행
if dfs(grid, visited, path, 0, 0):
  print("YES")
  # 성공 시 경로 출력
  for step in path:
    print(f"({step[0]},{step[1]})", end=' ')
  print("→ 0 도달 → 성공")
else:
  print("NO") # 실패 시 NO 출력