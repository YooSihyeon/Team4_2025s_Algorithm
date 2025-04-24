
# grid 예시대로 설정
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


 #dfs 를 사용해서 위치 탐색, x,y는 그리드의 위치를 의미함.
def dfs (x, y,target) :
            # 그리드의 길이 계산
        grid_n = len(grid)
        
        #방문 전인지 확인
        visited = [[False]*grid_n for _ in range(grid_n)]
        
        # path 기록 저장
        path = []

        # 모든 path 기록 저장
        all_paths =[]
    # 범위 밖에 있거나 이미 방문했으면 False 반환
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
            return False

        if grid[x][y] == target:
            # 경로에 해당하는 숫자값들의 합 계산
            value_sum = sum(grid[i][j] for i, j in path)
            all_paths.append((list(path), value_sum))  # 경로와 합 저장
            path.pop()
            visited[x][y] = False
            return True
        
        step = grid[x][y]

        # 상하좌우 탐색
        found = False
        for dx, dy in [(-step, 0), (step, 0), (0, -step), (0, step)]:
            if dfs(x + dx, y + dy, target):
                found = True

        path.pop()               # 백트래킹
        visited[x][y] = False 
 
        # 만약 경로가 아닌 경우 다시 돌아가야함 
        # 실패한 경로는 지워짐. 이전 위치로 돌아가게 됨.
        
        return found

 # 시작 위치에서 dfs 호출
dfs(0,0,0)


