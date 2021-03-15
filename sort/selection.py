import random

data_list = random.sample(range(100), 50)

def selection_sort(data_list):
    for stand in range(len(data_list) -1):
        lowest = stand

        for num in range(stand, len(data_list)):
            if data_list[lowest] > data_list[num]:
                lowest = num
        data_list[stand], data_list[lowest] = data_list[lowest], data_list[stand]

    return data_list        
    

if __name__ == "__main__":
    result = selection_sort(data_list)
    print(result)