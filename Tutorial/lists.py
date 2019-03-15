# Lists use brackets

l1 = ['physics', 'chemistry', 1997, 2000]
l2 = [1,2,3,4,5]
l3 = ["a", "b", "c", "d"]

print ("The first list is: ", l1)
print ("The last element of the list is: ", l3[-1])

# Updating 
l1[0] = 'biology'
print (l1)

# Delete
print (l2)
del l2[4]
print (l2)

# Operations
print ("The length of this list is: ", len(l1))
print (l1 + l2)
print (l3 * 2)
print ("Is 2 in l2?", '\n', 2 in l2)


a = [1,2,3,4,5]
b = [3,4,5,7,2]
# More operations
# In python3, cmp doesn't exist
# cmp(a,b) is replaced by the following expression: (a>b)-(a<b)
# Returns -1 if a<>b
print((a>b)-(a<b))
print(a!=b)
# list(seq): convert tuple into a list

