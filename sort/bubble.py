import random

data_list = random.sample(range(100), 50)

def bubble_sort(data):
    for i in range(len(data_list)):
        swap = 0
        for j in range(len(data_list) - 1 - i):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                swap += 1
        
        if swap == 0:
            break
    return data_list

if __name__ == "__main__":
    result = bubble_sort(data_list)
    print(result)
    