# Matrix is a 2D array where each row is of exactly same size
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
print (a)    
m = reshape(a,(7,5))
print(m)

# Accessing values in a matrix
print (m[2])
print (m[2][3])

# Adding a row
# new = append(old,[the row being added], 0 for row)
m_r = append(m,[['Avg',12,15,13,11]],0)
print (m_r)

# Adding a column
# new = insert(old, [column #], [[element], ...], 1 for col)
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print (m_c)

# Deleting a row from a matrix
# delete(arr, obj, axis=None)
# 0 for axis = row
m_r = delete(m, [7], 0)
print (m)

# Deleting a column
# delete(arr, obj, axis=None)
# 1 for axis = col
m_c = delete(m, s_[4], 1)
print (m)

# Updating a row
# The same as updating any 2d array, so long as the size is correct