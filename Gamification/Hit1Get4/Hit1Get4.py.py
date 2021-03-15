import socket
import time
import math

def getAngle(x1, y1, x2, y2):
    # x1, y1 수구 좌표
    # x2, y2 목적구 좌표
    width = x2 - x1
    height = y2 - y1

    radian = math.atan2(height, width)

    if x1 >= x2 and y1 < y2:
        angle = 270 + (180 - 180 / math.pi * radian)
    
    elif x1 < x2 and y1 < y2:
        angle = 90 - 180 / math.pi * radian

    elif x1 < x2 and y1 >= y2:
        angle = 90 + abs(180 / math.pi * radian)

    elif x1 >= x2 and y1 >= y2:
        angle = 90 + abs(180 / math.pi * radian)

    distance = math.sqrt(width**2 + height**2)
    power = distance

    return angle, power



def get_targetDegree(x1, y1, x2, y2):
    # 수구 좌표 : x1, y1
    # 목적구 좌표 : x2, y2
    width = x2 - x1
    height = y2 - y1

    radian = math.atan2(height, width)

    if x1 >= x2 and y1 < y2:
        degree = 180 - (180 / math.pi * radian)
        direction = 1
    
    elif x1 < x2 and y1 < y2:
        degree = 180 / math.pi * radian
        direction = 1

    elif x1 < x2 and y1 >= y2:
        degree = 90 - abs(180 / math.pi * radian)
        direction = -1

    elif x1 >= x2 and y1 >= y2:
        degree = abs(180 / math.pi * radian) - 90
        direction = -1

    return degree, direction


def get_holeDegree(x1, y1, x2, y2):
    # 원점 좌표 : x1, y1
    # 목적지 좌표 : x2, y2
    width = x2 - x1
    height = y2 - y1

    radian = math.atan2(height, width)
    distance = math.sqrt(width**2 + height**2)

    if x1 >= x2 and y1 < y2:
        degree = 180 - (180 / math.pi * radian)
    
    elif x1 < x2 and y1 < y2:
        degree = 180 / math.pi * radian

    elif x1 < x2 and y1 >= y2:
        degree = 90 - abs(180 / math.pi * radian)

    elif x1 >= x2 and y1 >= y2:
        degree = abs(180 / math.pi * radian) - 90

    return degree, distance

# User and Launcher Information
NICKNAME = 'DAEJEON02_OHSEUNGCHUL'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s/' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send('%d/%d' % (CODE_REQUEST, CODE_REQUEST).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    angle = 0.0
    power = 0.0

    ##############################
    # Begining of Your Code
    # Put your code here to set angle and power values.
    # angle(float) must be between 0.0 and 360.0
    # power(float) must be between 1.0 and 100.0
    beta = [0, 70, 55, 50, 45, 35, 30, 25, 20, 15, 10, 5, 0]

    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]

    if gameData.order == 1:
        target_num = [1, 3, 5]
    else:
        target_num = [2 ,4, 5]

    for i in target_num:
        if gameData.balls[i][0] != -1:
            targetBall_x = gameData.balls[i][0]
            targetBall_y = gameData.balls[i][1]

            tar_degree, tar_direction = get_targetDegree(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)

            if tar_direction == 1:
                hole_num = [3, 4, 5]
            else:
                hole_num = [0, 1, 2]

            for j in hole_num:
                hole_x = HOLES[j][0]
                hole_y = HOLES[j][1]

                if hole_x <= targetBall_x <= whiteBall_x or hole_x >= targetBall_x >= whiteBall_x:
                    hole_degree, _ = get_holeDegree(targetBall_x, targetBall_y, hole_x, hole_y)
                    if tar_degree > hole_degree:
                        sep_point = tar_degree - hole_degree
                    else:
                        sep_point = hole_degree - tar_degree
                    
                    new_point = 0
                    for k in range(1, len(beta)):
                        if beta[k]-2.5 <= sep_point < beta[k]+2.5:
                            new_point = 5.72 - (5.72 * k/12)

                    if tar_direction == 1:
                        angle, power = getAngle(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y - new_point)
                    elif tar_direction == -1:
                        angle, power = getAngle(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y + new_point)
            break
                
    # You can clear Stage 1 with the pre-written code above.
    # Those will help you to figure out how to clear other Stages.
    # Good luck!!
    # End of Your Code
    ##############################

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()
