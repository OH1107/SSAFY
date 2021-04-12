# DP 구현 방식 : recursive 방식

memo = [0,1]

def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]


###############################


# DP 구현 방식 : iterative 방식

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    
    return f[n]

# memoization을 재귀적 구조에 사용하는 것보다
# 반복적 구조로 DP를 구현하는 것이 성능면에서 보다 효율적

# 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문