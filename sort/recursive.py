def factorial(num):
    if num > 1:
        return num * factorial(num -1)
    else:
        return num

if __name__ == "__main__":
    for num in range(10):
        print (factorial(num))

# 시간 복잡도와 공간복잡도
# factorial(n)은 n-1번의 factorial()함수를 호출해서, 곱셈을 함
# 일종의 n-1번 반복문을 호출한 것과 동일
# O(n-1)이므로 O(n)   

# 재귀 호출의 일반적인 형태
# def function(입력):
#     if 입력 <= 일정값:  # 입력이 일정 값보다 작으면
#         return 결과값   # 재귀호출 종료
#     function(입력보다 작은 값)
#     return 결과값        