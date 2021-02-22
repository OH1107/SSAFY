# 재귀함수 피보나치수열

def fibo(n):
    arr[n] += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

arr = [0] * 35

# fibo(40)도 시간이 오래 소요
print(fibo(20))

# 재귀함수로 구현한 알고리즘은 문제점이 있음
# "엄청난 중복 호출이 존재"하는 것

print(arr)
print(sum(arr))

print('-' * 10)
# ----------

# Memoization
memo = [0,1]

def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

# 메모이제이션 활용 후, fibo1(40)도 바로 출력
print(fibo1(40))
print(memo)

###########################################
memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    
    return memo2[n]

print(fibo2(10))
print(memo2)
