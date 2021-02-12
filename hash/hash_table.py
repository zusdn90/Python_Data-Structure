import hashlib

hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
        
        
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
    
if __name__ == "__main__":
    save_data('Hong', '01012341234')
    save_data('Hyun', '01023432343')
    save_data('Woo', '01067676767')
    
    data = read_data('Woo')
    print(data)
    
    # SHA-1
    data = 'test'.encode()
    hash_object = hashlib.sha1()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    
    # SHA-256
    data = 'test'.encode()
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    