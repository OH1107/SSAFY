T = int(input())

x = 0
while x < T:
    n = int(input())
    num = 1
    
    null_list = [[0] * n for _ in range(n)]

    row_start_point = 0
    row_end_point = n - 1

    row_point = row_start_point

    col_start_point = 0
    col_end_point = n - 1

    col_point = col_start_point

    while True:
        # row 시작, col 시작인 경우
        if row_point == row_start_point and col_point == col_start_point:
            for i in range(col_start_point, col_end_point + 1):
                null_list[row_point][i] = num
                num += 1
            col_point = col_end_point
            row_start_point += 1
            row_point = row_start_point

        # row 시작, col 끝인 경우
        elif row_point == row_start_point and col_point == col_end_point:
            for i in range(row_start_point, row_end_point + 1):
                null_list[i][col_point] = num
                num += 1
            row_point = row_end_point
            col_end_point -= 1
            col_point = col_end_point

        # row 끝, col 끝인 경우
        elif row_point == row_end_point and col_point == col_end_point:
            for i in range(col_end_point, col_start_point - 1, -1):
                null_list[row_point][i] = num
                num += 1
            col_point = col_start_point
            row_end_point -= 1
            row_point = row_end_point
        
        # row 끝, col 시작인 경우
        elif row_point == row_end_point and col_point == col_start_point:
            for i in range(row_end_point, row_start_point-1, -1):
                null_list[i][col_point] = num
                num += 1
            row_point = row_start_point
            col_start_point += 1
            col_point = col_start_point
        
        if num == n * n + 1:
            break
    
    print(f"#{x+1}")
    for i in range(n):
        for j in range(n):
            print(null_list[i][j], end=" ")
        print()
        
    x += 1