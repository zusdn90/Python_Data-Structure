import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
        
class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break            
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
                
    def search(self, value):
        self.current_node = self.head
        
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        
        return False 
    
    def delete(self, value):
        searched = False
        self.current_node, self.parent = self.head, self.head
        
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
                
        if searched == False:
            return False
        
        
        # Case1: 삭제할 노드가 Leaf Node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
                
        # Case2: 삭제할 Node가 Child Node를 한개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
                
        # Case3: 삭제할 Node가 Child Node를 두 개 가지고 있을 경우(삭제할 Node가 Parent Node 왼쪽에 있을 때)                                                   
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                
                self.change_node_parent.left = None
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.change_node_parent
                self.change_node.left = self.current_node.left  
            # Case3: 삭제할 Node가 Child Node를 두 개 가지고 있을 경우(삭제할 Node가 Parent Node 오른쪽에 있을 때)        
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                
                self.change_node_parent.left = None
                
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                
                self.parent.left = self.change_node
                self.change_node.right = self.change_node_parent
                self.change_node.left = self.current_node.left
        
        return True      
            
if __name__ == "__main__":
    bst_nums = set()
    
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    
    head = Node(500)
    binary_tree = NodeMgmt(head)
    
    for num in bst_nums:
        binary_tree.insert(num)
        
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print('search faild', num)
            
            
    delete_nums = set()
    bst_nums = list(bst_nums)
    
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])
        
    for del_num in delete_nums:
        if binary_tree.delete(del_num) == False:
            print('search failed', delete_nums, del_num)
            
            
        