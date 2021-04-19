# 첫 줄에는 트리의 노드의 총 수 V가 주어짐
# 그 다음 줄에는 V-1개 간선이 나열
# 간선은 그것을 이루는 두 정점으로 표기되며, '부모-자식'순서로 표기

# 아래의 예에서 두 번째 줄 처음 1 2는 정점 1과 2를 잇는 간선을 의미
# 1이 부모, 2가 자식을 의미
# 간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열

v = 13  # 노드의 수
data = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'   # 부모-자식 쌍
n = 12  # 간선의 수

# 이진 트리를 전/중/후위 순회하고 방문한 노드의 번호를 출력


# 전위 순회
def preorder(v):
    if v != 0:
        print(v, end=' ')
        preorder(left_c[v])
        preorder(right_c[v])


# 중위 순회
def inorder(v):
    if v != 0:
        inorder(left_c[v])
        print(v, end=' ')
        inorder(right_c[v])


# 후위 순회
def postorder(v):
    if v != 0:
        postorder(left_c[v])
        postorder(right_c[v])
        print(v, end=' ')


_data = list(map(int, data.split(' ')))

left_c = [0] * (v+1)
right_c = [0] * (v+1)
par = [0] * (v+1)

for i in range(n):
    p_node, c_node = _data[i*2], _data[i*2+1]

    if left_c[p_node] == 0:
        left_c[p_node] = c_node

    else:
        right_c[p_node] = c_node

    par[c_node] = p_node

for i in range(1, v):
    if par[i] == 0:
        root = i
        break


print('전위 순회 : ', end='')
preorder(root)
print()

print('중위 순회 : ', end='')
inorder(root)
print()

print('후위 순회 : ', end='')
postorder(root)
print()
