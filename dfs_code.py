
## dfs 코드 ##
#0. 예시 그래프 입력
graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

#1. 스택/큐를 이용한 DFS 구현
def dfs(graph, start_node):

    # 두개의 리스트를 별도로 관리해줌 (방문 전과 방문 후)
    need_visited, visited = list(), list()

    # 시작 노드 설정
    need_visited.append(start_node)

    # 방문을 아직 안한 노드가 있다면,
    while need_visited:
        
        # 가장 마지막 데이터 추출 (스택 구조 활용)
        node = need_visited.pop()

        # 만약 방문한 목록에 없으면 ?
        if node not in visited:

            # 방문 리스트에 추가
            visited.append(node)

            #그 노드에 연결된 노드를 방문 전 노드에 추가
            need_visited.extend(graph[node])

    return visited


# 결과 확인
dfs(graph,'A')
print(dfs(graph, 'A'))


#2. deque를 활용한 DFS 구현
def dfs2(graph, start_node):
    
    #deque 패키지 불러오기
    from collections import deque
    visited =[]
    need_visited = deque()

    #시작 노드 설정
    need_visited.append(start_node)

    # 방문 전 리스트 확인
    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            #방문 후 리스트에 노드 추가
            visited.append(node)
            #인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
        
    return visited
    
# 결과 확인
dfs2(graph,'A')
print(dfs2(graph, 'A'))

#3. 재귀함수를 통한 DFS 구현
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited


# 결과 확인
dfs_recursive(graph,'A')
print(dfs_recursive(graph, 'A'))
