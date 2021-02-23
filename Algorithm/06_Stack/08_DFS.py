# 비선형구조 그래프의 모든 자료를 빠짐없이 검색하는 방법
# 깊이 우선 탐색(Depth First Search, DFS)

# 1. 시작 정점으로부터 한 방향으로 갈 수 있는 경로가 있는 깊이까지 탐색
# 2. 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 후퇴
# 3. 갈림길에서 다른 방향의 정점으로 탐색을 이어 진행
# 4. 반복하여 모든 정점을 방문하는 순회방법

# 가장 마지막에 만났던 갈림길의 정점으로 되돌아가기 위해
# 후입선출 구조의 스택 사용

# input
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 재귀함수 구조의 dfs
def dfs1(v):
    visited[v] = 1
    print(v, end = ' ')

    for w in range(n+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs1(w)


# 반복구조의 dfs
def dfs2(v):
    res = []    # 방문순서를 저장할 리스트
    s = []      # 스택 생성
    s.append(v) # push(v) 시작점 저장
    
    while len(s) != 0:  # 스택이 비어있지 않는 경우
        n = s.pop()     # pop(), 갈 수 있는 노드 중 하나를 꺼내 이동

        if visited[n] == 0:
            visited[n] = 1  # 방문했음을 표시
            res.append(n)
            for i in range(N+1):
                if adj[n][i] == 1:  # i와 인접해있다면
                    s.append(i)     # 스택 목록 추가
    return res

N, e = map(int, input().split())
arr = list(map(int, input().split()))

adj = [[0] * (N+1) for i in range(N+1)] # 간선의 정보를 인접행렬에 저장 (2중 리스트)
visited = [0] * (N+1) # 방문 여부를 체크하는 리스트

for i in range(0, len(arr), 2): # 인접행렬 작성(1 2가 들어오면 1, 2와 2, 1에 1)
    v1 = arr[i]
    v2 = arr[i+1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

print(dfs2(1))