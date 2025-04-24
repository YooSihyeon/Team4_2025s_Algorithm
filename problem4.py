# 문제 4번.

#1. grid 설정
grid = [
    [3, 4, 1, 2, 5, 2, 3, 2, 1, 1],
    [1, 2, 3, 2, 1, 4, 2, 2, 3, 2],
    [2, 1, 1, 3, 2, 1, 1, 3, 1, 2],
    [3, 2, 4, 2, 3, 1, 2, 1, 4, 2],
    [1, 3, 2, 1, 1, 2, 4, 3, 2, 3],
    [2, 2, 1, 4, 3, 3, 1, 2, 3, 1],
    [1, 1, 2, 1, 2, 4, 3, 1, 2, 1],
    [3, 3, 1, 2, 3, 1, 1, 4, 2, 2],
    [2, 1, 2, 3, 2, 2, 1, 2, 3, 1],
    [1, 2, 1, 1, 1, 1, 1, 3, 2, 0]  # (9, 9)이 도착점
]


# 알고리즘 설계
def problem4 (grid):
    # 그리드의 길이 계산
    grid_n = len(grid)
    
    #방문 전인지 확인
    visited = [[False]*grid_n for _ in range(grid_n)]
    
    # path 기록 저장
    path = []
    
    # 모든 path 기록 저장
    all_paths = []

    #dfs 를 사용해서 위치 탐색, x,y는 그리드의 위치를 의미함.
    def dfs (grid, x, y, visited, path, all_paths) :
    # 범위 밖에 있거나 이미 방문했으면 False 반환
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
            return
        path.append((x, y))
        visited[x][y] = True

        if grid[x][y] == 0:
            all_paths.append(list(path))  # 경로 복사해서 저장

        else:
            # 상하좌우로 탐색
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(grid, x+dx, y+dy, visited, path, all_paths)
        
        # 백트래킹
        path.pop()
        visited[x][y] = False


    if dfs(0, 0):
        #dfs결과가 true면 yes라고 출력
        print("YES")
        # path의 결과들을 route로 연결
        route = " → ".join(f"({x},{y})" for x, y in path)
        # 예시 처럼 출력
        print(f"{route} → 0 도달 → 성공")
    else: # dfs 결과가 false이면 no라고 출력
        print("NO")
    return all_paths

problem4(grid)


#1. 탈출 가능한 모든 경로 출력하기
def dfs(grid, x, y, target, visited, path, all_paths):
    # 범위를 벗어나거나 이미 방문했으면 return
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
        return
    
    path.append((x, y))
    visited[x][y] = True
    
    if grid[x][y] == target:
        all_paths.append(list(path))  # 경로 복사해서 저장
    else:
        # 상하좌우로 탐색
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(grid, x+dx, y+dy, target, visited, path, all_paths)
    
    # 백트래킹
    path.pop()
    visited[x][y] = False

def find_all_paths(grid, target):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    all_paths = []
    dfs(grid, 0, 0, target, visited, [], all_paths)
    return all_paths

#2. 그중 가장 짧은 경로 선택
#3. 그 경로 숫자 의 합 구하기 (정답)