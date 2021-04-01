input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    # 메모에 있는지 확인
    if n in fibo_memo:
        return fibo_memo[n]
    # 없으면 메모에 기록
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    # 있으면 가져와서 사용
    return nth_fibo


print(fibo_dynamic_programming(input, memo))