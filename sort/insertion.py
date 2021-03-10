import random

data_list = random.sample(range(100), 50)

def insertion_sort(data):
    for stand in range(len(data_list)):
        key = data_list[stand]
        for num in range(stand, 0, -1):
            if key < data_list[num -1]:
                data_list[num -1], data_list[num] = data_list[num], data_list[num-1]
            else:
                break
    return data_list

if __name__ == "__main__":
    result = insertion_sort(data_list)
    print(result)