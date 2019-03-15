from array import *

# Arrays use brackets
a1 = array('i', [0,1,2,3,4,5,6,7,8,9])

print(a1)
print('\n')

# Accessing specific element
print ("Printing the first element of array 1", a1[0], '\n')

# Insertion
a1.insert(1,9)
print("Inserted 9 at the 2nd place")
print(a1[0:2], '\n')

# Deletion
# Doesn't take care of redundancy
a1.remove(9)
print(a1)

# Search
# Returns the element at the index
print(a1.index(8))

# Update
# Assigns a new value to the index
a1[5] = 9
print(a1)