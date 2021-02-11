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
        
        # 1. self.head를 삭제해야할 경우 - self.head를 바꿔야함.
        if self.head.data == data:
            # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제
            temp = self.head
            # 만약 self.head 객체를 삭제하면 self.head.next에서 오류남.
            self.head = self.head.next
            del temp
        else:
            node = self.head
            # 2. self.head가 아닌 노드를 삭제해야할 경우
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
                    
        
if __name__ == "__main__":
    node_mgmt = NodeMgmt(0)
    
    for data in range(1, 10):
        node_mgmt.add(data)
    
    node = node_mgmt.search_node(4)
    print(node.data)
    