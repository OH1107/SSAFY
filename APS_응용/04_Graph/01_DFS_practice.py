# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이우선 탐색 경로를 출력하시오.
# 시작 정점은 1로 시작

# 반복 dfs
def dfs(v):
    global res

    s = [v]
    while s:
        tmp = s.pop()
        if not visited[tmp]:
            visited[tmp] = 1
            res.append(tmp)
            for w in range(n+1):
                if adj[tmp][w] and not visited[w]:
                    s.append(w)


# 재귀 dfs
def dfs_recursive(g, v):
    global recur_res
    recur_visited[v] = 1
    recur_res.append(v)
    for w in range(n+1):
        if adj[v][w] and not recur_visited[w]:
            dfs_recursive(g, w)


data = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
n = 7
adj = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    n1, n2 = data[i*2], data[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

visited = [0] * (n+1)
recur_visited = [0] * (n+1)

res = []
recur_res = []

dfs(1)
print(*res)
# => 1 3 7 6 5 2 4

dfs_recursive(adj, 1)
print(*recur_res)
# => 1 2 4 6 5 7 3