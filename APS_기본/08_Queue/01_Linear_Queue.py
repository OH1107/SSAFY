# 선형 큐에서 front와 rear의 초기값은 -1
front, rear = -1, -1

# 삽입
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = item

# 삭제
def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front += 1
        return Q[front]

# 공백상태 검사
def isEmpty():
    return front == rear

# 포화상태 검사
def isFull():
    return rear == len(Q) - 1

# 검색
def Qpeek():
    if isEmpty():
        print('Queue_Empty')
    else:
        return Q[front+1]