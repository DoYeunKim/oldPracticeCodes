# Nodes = pointers

# Node created as class called daynames
class daynames:
    # Constructor
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')

e1.nextval = e2
e2.nextval = e3

# Traversing the node elements
thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval
print()