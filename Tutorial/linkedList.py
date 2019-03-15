class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end=" ")
            printval = printval.nextval
        print()

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        # If the linked list is empty, the new node is the new head
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
    
    def InBetween(self, newdata, middle_node_val):
        NewNode = Node(newdata)
        searchVal = self.headval
        while searchVal is not None:
            if searchVal.dataval == middle_node_val:
                break
            if searchVal.nextval is None:
                print("The mentioned node is absent")
                return
            searchVal = searchVal.nextval
        
        NewNode = Node(newdata)
        NewNode.nextval = searchVal.nextval
        searchVal.nextval = NewNode

    def removeNode(self, removeKey):
        headVal = self.headval

        if headVal is not None:
            if headVal.dataval == removeKey:
                self.headval = headVal.nextval
                headVal = None
                return
            
        while headVal is not None:
            if headVal.dataval == removeKey:
                break
            prev = headVal
            headVal = headVal.nextval

        if headVal == None:
            return
        
        prev.nextval = headVal.nextval

        headVal = None



list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3

list1.listprint()

list1.AtBegining("Sun")
list1.listprint()

list1.AtEnd("Fri")
list1.listprint()

list1.InBetween("Thu", "Wed")
list1.listprint()

list1.removeNode("Tue")
list1.listprint()

# Doubly linked list

class dNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class doubly_linked_list:
    def __init__(self):
        self.head = None

    # Add data elements
    def push (self, NewVal):
        NewNode = dNode(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Inserting
    def insert (self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = dNode(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    # append to the doubly linked list
    def append (self, NewVal):
        NewNode = dNode(NewVal)
        NewNode.next = None
        
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return



    # print the doubly linked ist
    def listprint(self, node):
        while node is not None:
            print (node.data, end= " ")
            last = node
            node = node.next
        print()


dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
dllist.insert( dllist.head.next, 13)
dllist.listprint(dllist.head)
dllist.append(18)
dllist.listprint(dllist.head)
