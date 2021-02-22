# Counting_sort 카운팅 소트를 이용한 Baby_gin
num = 133111 # Baby Gin 확인할 6자리 수
cnt_list = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    cnt_list[num % 10] += 1
    num //= 10

i = 0
tri = False
run = False

while i < 10:
    # triplete 조사 후 데이터 삭제 과정
    if cnt_list[i] >= 3:
        cnt_list[i] -= 3
        tri = True
        continue

    # run 조사 후 데이터 삭제 과정
    if cnt_list[i] >= 1 and cnt_list[i+1] >= 1 and cnt_list[i+2] >= 1:
        cnt_list[i] -= 1
        cnt_list[i+1] -= 1
        cnt_list[i+2] -= 1
        run = True
        continue
    i += 1

if run and tri:
    print("Baby Gin")
else:
    print("None")