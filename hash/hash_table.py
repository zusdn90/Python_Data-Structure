hash_table = list([i for i in range(10)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
    
if __name__ == "__main__":
    save_data('Hong', '01012341234')
    save_data('Hyun', '01023432343')
    save_data('Woo', '01067676767')
    
    data = read_data('Hyun')
    print(data)