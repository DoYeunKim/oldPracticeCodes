import collections

d1 = {'d1': 'Mon', 'd2': 'Tue'}
d2 = {'d3': 'Wed', 'd4': 'Thu'}

# collections.ChainMap(base, other dictionary)
res = collections.ChainMap(d1, d2)

print (res)
print (res.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('d3 in res: {}'.format(('d3' in res)))
print('d4 in res: {}'.format(('d4' in res)))


# Map Reordering
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res1 = collections.ChainMap(dict1, dict2)

print(res1.maps,'\n')

res2 = collections.ChainMap(dict2, dict1)

print(res2.maps,'\n')


# Updating map
# When the content of a dictionary is updated, the ChainMap is also updated
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)

print(res.maps,'\n')

dict2['day4'] = 'Fri'

print(res.maps,'\n')