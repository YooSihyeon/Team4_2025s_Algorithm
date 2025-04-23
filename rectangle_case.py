# 더 복잡한 경우 연습해보기
# 1. grid가 직사각형이라면 ?

# 그리드 설
grid = [
    [1,1,1,1],
    [5,6,7,0]
]


# 기본 문제에서 코드 수정해보기
def p4_sh (grid):
    # 그리드가 정사각형이 아닌 직사각형이라면 index 에러가 발생할 수 있음. 
    rows = len(grid)
    cols = len(grid[0])
    # 열과 행을 구분해서 저장해야함.
    
    #방문 전인지 확인
    ## 직사각형인 경우는 False가 열 만큼, 범위는 행 만큼으로 변경
    visited = [[False]*cols for _ in range(rows)]
    
    # path 기록 저장
    path = []

    #dfs 를 사용해서 위치 탐색, x,y는 그리드의 위치를 의미함.
    def dfs (x, y) :
    # 범위 밖에 있거나 이미 방문했으면 False 반환
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        #이미 방문했으면 False 반환
        if visited[x][y]:
            return False
        path.append((x,y)) # path에 경로 저장
        # 처음 시작 좌표 값이 0이면 True 반환
        if grid[x][y] == 0:
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
        # 예시 처럼 출력
        print(f"{route} → 0 도달 → 성공")
    else: # dfs 결과가 false이면 no라고 출력
        print("NO")

p4_sh(grid)

