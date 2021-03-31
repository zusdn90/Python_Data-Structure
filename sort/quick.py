import random

def quick(data_list):
    if len(data_list) <= 1:
        return data_list

    pivot = data_list[0]
    left = []
    right = []

    # for index in range(1,len(data_list)):
    #     if data_list[index] < pivot:
    #         left.append(data_list[index])
    #     else:
    #         right.append(data_list[index])   

    left = [data for data in data_list[1:] if data <= pivot]
    right = [data for data in data_list[1:] if data > pivot]
    
    return quick(left) + [pivot] + quick(right)

if __name__ == "__main__":
    data_list = random.sample(range(100), 10)       
    result = quick(data_list)

    print(result)    