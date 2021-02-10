class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
                    
        
if __name__ == "__main__":
    linked_list1 = NodeMgmt(0)
    linked_list1.desc()
    
    print(linked_list1.head)
    
    linked_list1.delete(0)
    print(linked_list1.head)
    
    linked_list1 = NodeMgmt(0)
    linked_list1.desc()
    
    for data in range(1,10):
        linked_list1.add(data)
    linked_list1.desc()
    linked_list1.delete(4)
    linked_list1.desc()