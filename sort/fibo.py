# recursive call 활용
def fibo(num):
    if num <=1:
        return num
    return fibo(num-1) + fibo(num-2)        

# 동적 계획법 활용
def fibo_dp(num):
    cache = [0 for index in range(num + 1)]
    print(cache)
    cache[0] = 0
    cache[1] = 1
    print(cache)

    for index in range(2, num + 1):
        cache[index] = cache[index -1] + cache[index -2]
    return cache[num]

if __name__ == "__main__":
    result = fibo(10)
    print(result)

    result = fibo_dp(10)
    print(result)