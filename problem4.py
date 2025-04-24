
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


def problem4 (grid):
    # 그리드의 길이 계산
    grid_n = len(grid)
    
    #방문 전인지 확인
    visited = [[False]*grid_n for _ in range(grid_n)]
    
    # path 기록 저장
    path = []

    # 모든 path 기록 저장
    all_paths =[]

    #dfs 를 사용해서 위치 탐색, x,y는 그리드의 위치를 의미함.
    def dfs (x, y,target) :
    # 범위 밖에 있거나 이미 방문했으면 False 반환
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
            return
        path.append((x, y))
        visited[x][y] = True
        if grid[x][y] == target:
            # 경로에 해당하는 숫자값들의 합 계산
            value_sum = sum(grid[i][j] for i, j in path)
            all_paths.append((list(path), value_sum))  # 경로와 합 저장

        path.pop()

        # 방문한 좌표들을 true로 설정 (원래 모두 false 였음)
        visited[x][y] = True 
        # 그리드의 숫자 만큼 이동 하므로
        # 걸음 수를 그리드의 숫자로 저장
        step = grid[x][y]

        # 상하좌우 순으로 탐색, 재귀 함수 호출
        if (dfs(x - step, y,0) or
            dfs(x + step, y,0) or
            dfs(x, y - step,0) or
            dfs(x, y + step,0)):
            return all_paths
        # 만약 경로가 아닌 경우 다시 돌아가야함 
        # 실패한 경로는 지워짐. 이전 위치로 돌아가게 됨.


        return 



    return all_paths 

problem4(grid)


