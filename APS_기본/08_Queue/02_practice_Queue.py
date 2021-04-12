# 큐를 구현하여 다음 동작을 확인

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

Q = [0] * 3             # => [0, 0, 0]
rear, front = -1, -1

## 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입

enQueue(1)              # => [1, 0, 0]
print(Q)                # rear = 0

enQueue(2)              # => [1, 2, 0]
print(Q)                # rear = 1

enQueue(3)              # => [1, 2, 3]
print(Q)                # rear = 2

enQueue(4)              # rear == len(Q)-1 => Queue_Full
print('-' * 8) 

## 큐에서 세 개의 데이터를 차례로 꺼내서 출력

print(deQueue())        # => 1 / front = 0
print(deQueue())        # => 2 / front = 1
print(deQueue())        # => 3 / front = 2
deQueue()               # front == rear => Queue_Empty