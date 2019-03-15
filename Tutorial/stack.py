class Stack:
    def __init__ (self):
        self.stack = []

    def add (self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else: 
            return self.stack.pop()


s1 = Stack()
s1.add("Mon")
s1.add("Tue")
s1.peek()
print(s1.peek())
s1.add("Wed")
s1.add("Thu")
print(s1.peek())
s1.add("Sat")
print(s1.remove())
print(s1.peek())