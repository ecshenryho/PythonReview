# Key-value pairs, keys are unique while values may not be.
# The values can be of any type
# The keys must be an immutable data type such as strings, numbers, or tuples

# Declaration and accessing dictionary
dict1 = {'Brand': 'Toyota', 'Year': '2015', 'Model': 'Rave4'}
print(dict1['Brand'])
print(dict1['Year'])
print(dict1['Model'])

# Updating dictionary
dict1['Brand'] = "Honda"
print(dict1)
dict1['Miles'] = "20000 miles" # add new entry to dictionary
print(dict1)

# Delete dictionary elements
dict2 = dict1
print(dict2)
del dict2['Miles']  # delete elements by keys
print(dict2)
dict2.clear()  # remove all elements in dictionary
print(dict2)
del dict2    # delete the entire dictionary

# Properties of dictionary keys
# 1. keys are unique, when duplicate the last assignment wins
dict3 = {'Name': 'name', 'Age': '29', 'Name': 'Henry'}
print(dict3) # will print out: {'Name': 'Henry', 'Age': '29'}
# 2. Keys must be immutable ['key] is not allowed
dict4 = {['Name']: 'Henry', 'Age': 7}
print(dict4) # errors
