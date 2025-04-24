
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
    def dfs (x, y) :
    # 범위 밖에 있거나 이미 방문했으면 False 반환
        if not (0 <= x < grid_n and 0 <= y < grid_n):
            return False
        #이미 방문했으면 False 반환
        if visited[x][y]:
            return False
        path.append((x,y)) # path에 경로 저장
        # 처음 시작 좌표 값이 0이면 True 반환
        if grid[x][y] == 0:
            all_paths.append(list(path)) 
            return True

        # 방문한 좌표들을 true로 설정 (원래 모두 false 였음)
        visited[x][y] = True 
        # 그리드의 숫자 만큼 이동 하므로
        # 걸음 수를 그리드의 숫자로 저장
        step = grid[x][y]

        # 상하좌우 순으로 탐색, 재귀 함수 호출
        if (dfs(x - step, y) or
            dfs(x + step, y) or
            dfs(x, y - step) or
            dfs(x, y + step)):
            return True
        # 만약 경로가 아닌 경우 다시 돌아가야함 
        # 실패한 경로는 지워짐. 이전 위치로 돌아가게 됨.
        path.pop() 

        return False

    if dfs(0, 0):
        #dfs결과가 true면 yes라고 출력
        print("YES")
        # path의 결과들을 route로 연결
        route = " → ".join(f"({x},{y})" for x, y in path)
        # 모든 가능한 path출력하기
        print(all_paths)
        # 예시 처럼 출력
        print(f"{route} → 0 도달 → 성공")
        
    else: # dfs 결과가 false이면 no라고 출력
        print("NO")

problem4(grid)