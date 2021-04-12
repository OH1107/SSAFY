T = int(input())

x = 0
while x < T:
    n = int(input())
    
    route = [list(map(int, input().split())) for _ in range(n)]
    station = int(input())
    station_list= [int(input()) for _ in range(station)]
    result = [0] * station

    for i in range(len(route)):
        for j in range(len(station_list)):
            if station_list[j] >= route[i][0] and station_list[j] <= route[i][1]:
                result[j] += 1

    print(f'#{x+1} {" ".join(map(str, result))}')

    x += 1