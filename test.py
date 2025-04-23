import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 늘리기 (기본 1000이라 큰 격자에서 오류날 수 있음)

# 8방향 이동 정의 (상, 하, 좌, 우, 대각선 네 방향)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

# DFS 함수 정의
def dfs(grid, visited, path, x, y):
    n = len(grid)  # 격자 크기

    # 격자 범위 밖이면 리턴 False
    if not (0 <= x < n and 0 <= y < n):
        return False

    # 이미 방문한 좌표면 무한 루프 가능성 → 리턴 False
    if visited[x][y]:
        return False

    path.append((x, y))       # 현재 위치를 경로에 추가
    visited[x][y] = True      # 방문 처리

    # 종료 조건: 0을 만났으면 탈출 성공
    if grid[x][y] == 0:
        return True

    jump = grid[x][y]  # 현재 칸의 숫자만큼 이동 가능

    # 8방향으로 이동 시도
    for dx, dy in directions:
        nx, ny = x + dx * jump, y + dy * jump  # 점프한 다음 위치 계산
        if dfs(grid, visited, path, nx, ny):  # 재귀적으로 탐색
            return True  # 하나라도 성공하면 True 리턴

    # 이 경로는 실패했으므로 되돌리기 (백트래킹)
    path.pop()
    return False

# 메인 함수
def main():
    n = int(input())  # 격자 크기 입력
    grid = [list(map(int, input().split())) for _ in range(n)]  # 숫자 격자 입력
    visited = [[False]*n for _ in range(n)]  # 방문 여부 저장용 2차원 리스트
    path = []  # 이동 경로 저장용 리스트

    if dfs(grid, visited, path, 0, 0):  # (0,0)에서 시작
        print("YES")
        for step in path:
            print(f"({step[0]},{step[1]})", end=' ')
        print("→ 0 도달 → 성공")
    else:
        print("NO")

#main()
