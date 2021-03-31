import random

# 리스트를 앞뒤로 짜르는 함수
def split_func(data_list):
    if len(data_list) <= 1:
        return data_list
    
    medium = int(len(data_list) // 2)
    
    left = split_func(data_list[:medium])
    right = split_func(data_list[medium:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            sorted_list.append(right[right_point])
            right_point += 1
        else:
            sorted_list.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        sorted_list.append(left[left_point])
        left_point += 1

    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        sorted_list.append(right[right_point])
        right_point += 1        

    return sorted_list

if __name__ == "__main__":
    data_list = random.sample(range(100), 10)
    
    result = split_func(data_list)
    print(result)

    