# 원형 큐에서 front와 rear의 초기값은 0
front, rear = 0, 0

# Index의 순환을 위해서 front와 rear은 n-1 다음에 0으로 이동해야함
# 이를 위해 나머지 연산자 mod()를 사용

# 삽입
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item
    
# 삭제
def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

def delete():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)

# 공백상태 검사
def isEmpty():
    return front == rear

# 포화상태 검사
def isFull():
    return (rear + 1) % len(cQ) == front