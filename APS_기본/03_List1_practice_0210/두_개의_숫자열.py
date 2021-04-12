T = int(input())

i = 0
results = []

while i < T:
    NM = list(map(int, input().split()))
    
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    cycle = abs(NM[0] - NM[1])

    if len(n_list) > len(m_list):
        shorter = len(m_list)
        short_list = m_list[:]
        long_list = n_list[:]

    else:
        shorter = len(n_list)
        short_list = n_list[:]
        long_list = m_list[:]


    total_temp = 0
    for k in range(cycle+1):

        temp = 0
        total = 0
        for j in range(shorter):
            temp = short_list[j] * long_list[j+k]
            total += temp

        if total_temp < total:
            total_temp = total

    results.append(total_temp)
    i += 1

for idx, result in enumerate(results):
    print(f'#{idx+1} {result}')