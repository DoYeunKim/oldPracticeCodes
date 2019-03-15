class Queue:
    def __init__ (self):
        self.queue = list()

    def addtoq (self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    def size(self):
        return len(self.queue)

    def removefromq (self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in the queue!")

q1 = Queue()
q1.addtoq("Mon")
q1.addtoq("Tue")

# Deque: Double-ended queue
# Part of collections library
import collections
DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
print (DoubleEnded)

# append to the right
print("Adding to the right:")
DoubleEnded.append("Thu")
print(DoubleEnded)

# append to the left
print("Adding to the left:")
DoubleEnded.appendleft("Sun")
print(DoubleEnded)

# Remove from the right
print ("Removing from the right:")
DoubleEnded.pop()
print(DoubleEnded)

# Remove from the left
print ("Removing from the left:")
DoubleEnded.popleft()
print(DoubleEnded)

# Reverse the deque
print ("Reversing the deque:")
DoubleEnded.reverse()
print(DoubleEnded)