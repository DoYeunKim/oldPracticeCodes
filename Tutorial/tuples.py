# Tuples use parentheses
# Tuples cannot be changed

t1 = ('physics', 'chemistry', 1997, 2000)
# Empty tuple is written with empty parentheses e.g. t1 = ()
# A single element tuple requires a trailing comma e.g. t1 = (30, )

# Accessing values
print ("t1[1]: ", t1[1])

# Updating tuples
# Tuples are immutable as in the elements themselves cannot be changed
# However, we can update (concat) the tuples as a whole. e.g.:
t1 = (1, 2, 3)
t2 = (4,)
a = "t1 is: " + str(t1)
b = "t2 is: " + str(t2)
c = "And we cna merge them into t3: " + str(t1 + t2)
print (a + '\n' + b + '\n' + c +'\n')

# Deleting tuple elements
# We can only delete the entire tuple
print(t2)
del t2
#print (t2)

# Some operations
print (len(t1))
print (t1 * 2)
print ("Is 2 in t1?: ", 2 in t1)

