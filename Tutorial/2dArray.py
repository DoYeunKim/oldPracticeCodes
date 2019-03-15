from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print (T)

# Accessing values
print (T[0][1])
# Traverse through the rows
for r in T:
    # Traverse through the columns
    for c in r:
        # Instead of printing \n after each entry, just use an empty space
        print (c, end = " ")
    print()
print()


# Inserting values in 2D array
# TableName.insert(index/row, [the row being inserted])
T.insert(2, [0, 2, 3, 0])
for r in T:
    # Traverse through the columns
    for c in r:
        # Instead of printing \n after each entry, just use an empty space
        print (c, end = " ")
    print()
print()


# Deleting values in 2D array
# This again applies to an entire row
del T[2]
for r in T:
    # Traverse through the columns
    for c in r:
        # Instead of printing \n after each entry, just use an empty space
        print (c, end = " ")
    print()
print()

# To delete one specific value:
print (T[2])
del T[2][1]
print (T[2])
print ()