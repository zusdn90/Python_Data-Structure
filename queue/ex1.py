import queue



if __name__ == "__main__":
    
    data_queue = queue.Queue()
    data_queue.put("hello")
    data_queue.put(1)
    
    print(data_queue.qsize())
    print(data_queue.get())
    print(data_queue.qsize())
    print(data_queue.get())
    
    data_queue = queue.LifoQueue()
    data_queue.put("world")
    data_queue.put(1)
    
    print(data_queue.qsize())
    print(data_queue.get())
    
    data_queue = queue.PriorityQueue()
    
    data_queue.put((10, "pizza"))
    data_queue.put((5,1))
    data_queue.put((15,"chiken"))
    
    print(data_queue.qsize())
    print(data_queue.get())
    print(data_queue.get())
    print(data_queue.get())