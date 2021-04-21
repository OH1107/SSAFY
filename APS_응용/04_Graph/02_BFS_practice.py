# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 너비우선탐색하여 화면에 너비우선탐색 경로를 출력하시오.
# 시작 정점은 1로 시작하시오.


def bfs(g, v):   # 그래프 g, 탐색 시작점 v
    res = []
    q = [v]
    visited = [0] * (n + 1)
    visited[v] = 1

    while q:
        t = q.pop(0)
        res.append(t)

        for i in range(n+1):
            if adj[t][i] and not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    return res


data = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
n = 7
adj = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    n1, n2 = data[i*2], data[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

print(*bfs(adj, 1))

