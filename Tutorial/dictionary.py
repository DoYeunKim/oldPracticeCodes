# Dictionaries have keys and values, coupled by colons
# These couples are separated by commas
d1 = {'Name': "Alessandra", 'Age': 22, 'Class': 'Economy'}
print ("The name of the person is: " + d1['Name'])
print ("The age of this person is:", d1['Age'])
print (d1.keys())
print (d1.values())

# Updating dictionary
print ("Currently, the dictionary looks like this: ", d1)
print ("Lets update this dictionary")
d1['Name'] = "Alice"
d1['Age'] = 73
d1['Class'] = 'Prestige'
print ("The updated dictionary is: ", d1)

# Deleting dictionary elements
print (d1)
del d1['Name'] # Remove entry with the key
print ("Cleared name:", d1)
d1.clear() # Clears all entries in d1
print ("Cleared all: ", d1)
del d1

# Properties of dictionary keys
# 1. Only one entry per key is allowed
#   This means the the last entry for the said key will be the only one to be assigned
# 2. The keys must be immutable
#   e.g. d1 = {['Name']: 'Zara'} 
#   Here, ['Name'] is not a valid key


# Hash tables can be implemented with dictionary
