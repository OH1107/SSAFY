# 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것
# 모든 정점을 너비우선탐색하여 경로를 출력
# 시작 정점은 1

N = 7   # 정점의 개수
e = 8   # 간선의 개수

arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7 ,3, 7]  # 간선 정보

# 방문여부를 확인할 리스트
visited = [0] * (N+1) # 1에서 시작이므로 하나를 더 여유있게 줌

adj = [[0] * (N+1) for _ in range(N+1)]

# 인접행렬
for i in range(e):
    a = arr[i * 2]
    b = arr[i * 2 + 1]
    adj[a][b] = 1
    adj[b][a] = 1

# 방문 순서를 저장할 리스트
res = []

# 큐에 시작점을 두고 시작
q = [1]
visited[1] = 1

# 거리 측정을 위한 변수 
dis = 0

# 너비우선 탐색
while q:
    size = len(q)

    print('{} 거리의 정점 : {}'.format(dis, q))

    for i in range(size):
        tmp = q.pop(0)
        res.append(tmp)

        for i in range(N+1):
            if adj[tmp][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
    
    dis += 1

print('경로 순서 {}'.format(res))

# =>
# 0 거리의 정점 : [1]
# 1 거리의 정점 : [2, 3]
# 2 거리의 정점 : [4, 5, 7]
# 3 거리의 정점 : [6]
# 경로 순서 [1, 2, 3, 4, 5, 7, 6]