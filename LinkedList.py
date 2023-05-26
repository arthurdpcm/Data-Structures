class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def prepend(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def remove(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.prepend(0)
myList.display() #[0, 1, 2, 3]

myList.remove(2)
myList.display() #[0, 1, 3]

print(myList.search(1)) # True
print(myList.search(5)) # False

print(myList.isEmpty()) # False
myList.remove(1)
myList.remove(3)
myList.remove(0)
myList.display() # []
print(myList.isEmpty()) # True