class Node:
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

    # Inserting a new node
    # In this example, we are 
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data 

    def findVal(self, data):
        if self.data:
            if data == self.data:
                print (str(self.data) + ' is found\n')
            elif data < self.data:
                if self.left is None:
                    return str(data) + " Not Found\n"
                return self.left.findVal(data)
            else:
                if self.right is None:
                    return str(data) + "Not Found\n"
                return self.right.findVal(data)
                

    def printTree (self):
        if self.left:
            self.left.printTree()
        print(self.data, end = " ")
        if self.right:
            self.right.printTree()


root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print()
print(root.findVal(5))
print(root.findVal(3))

def bsearch(list, val):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size

    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if list[midval] == val:
            return val
        if val < list[midval]:
            idxn = midval - 1
        if val > list[midval]:
            idx0 = midval + 1
    
    if idx0 > idxn:
        return None

list = [2,6,7,9,15,25,37,72]

print(bsearch(list, 5))
print(bsearch(list, 15))