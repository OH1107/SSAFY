def BFS(G, v):          # 그래프 G, 탐색 시작점 v
    visited = [0] * n   # n : 정점의 개수
    queue = []          # 큐 생성
    queue.append(v)     # 시작점 v를 큐에 삽입

    while queue:                # 큐가 비어있지 않은 경우
        t = queue.pop(0)        # 큐의 첫번째 원소 반환
        if not visited[t]:      # 방문되지 않은 곳이라면
            visited[t] = True   # 방문한 것으로 표시
            visit(t)            # 필요한 행동을 취함
        
        for i in G[t]:          # t와 연결된 모든 선에 대해
            if not visited[i]:  # 방문되지 않은 곳이라면
                queue.append(i) # 큐에 넣기


# 완전그래프와 같이 간선이 많이 연결된 그래프일 경우
# 불필요한 계산을 막기위해서 다음과 같은 코드로 수정

def BFS(G, v):
    visited = [0] * n
    queue = []
    queue.append(v)
    visited[v] = True # 시작점을 방문했다고 먼저 선언

    while queue:

        size = len(queue)       # 이렇게 사이즈로 선언하면
        for i in range(size):   # 같은 거리인 정점들끼리 묶어서
            tmp = queue.pop(0)  # 필요 행동을 취할 수 있다.

            # 기존에는 방문 여부를 여기서 확인했음
            visit(t)            # 여기서 필요 행동만 취하고 방문 여부 확인은        
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True   # 방문 대상인 정점에 대해서 True로 미리 바꿔줌
