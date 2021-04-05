# 입력 예
# 3
# 1 2 1 3

# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

import sys
sys.stdin = open('input.txt', 'r')

def preorder(n):
    if n!=0:
        print(n, end=" ")
        preorder(child[n][0])
        preorder(child[n][1])

def inorder(n):
    if n!=0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])

def postorder(n):
    if n!=0:
        postorder(child[n][0])
        postorder(child[n][1])
        print(n, end=" ")

N=int(input())
arr=list(map(int, input().split()))
child=[[0]*2 for i in range(N+1)]

for i in range(N-1):
    if child[arr[i*2]][0]==0:
        child[arr[i*2]][0]=arr[i*2+1]
    else:
        child[arr[i*2]][1] = arr[i*2 + 1]

print("전위 순회 결과:", end=" ")
preorder(1)
print()

print("중위 순회 결과:", end=" ")
inorder(1)
print()

print("후위 순회 결과:", end=" ")
postorder(1)
print()

'''
전위 순회 결과: 1 2 4 7 12 3 5 8 9 6 10 11 13 
중위 순회 결과: 12 7 4 2 1 8 5 9 3 10 6 13 11 
후위 순회 결과: 12 7 4 2 8 9 5 10 13 11 6 3 1
'''