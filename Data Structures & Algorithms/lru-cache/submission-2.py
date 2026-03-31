class Node:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    def insert(self,node):
        previous=self.right.prev
        previous.next=node
        node.prev=previous
        node.next=self.right
        self.right.prev=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node=Node(key,value)
        self.insert(new_node)
        self.cache[key]=new_node
        if (len(self.cache)) > self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
