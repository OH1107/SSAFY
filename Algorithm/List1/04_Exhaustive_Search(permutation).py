N = 3
card = [4, 5, 6]

# 반복문을 이용해서 작성

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])