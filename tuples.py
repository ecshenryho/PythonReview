# A tuple is a sequence of immutable Python Object. Tuples are sequences just like list
# Tuples CAN NOT be changed, and use parentheses compares to list can be changed and using []

# Tuples declaration
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = ()
tup4 = (7,)  # must include comma with a single element Tuples
tup5 = 8, 9
tup6 = "string 1", "string 2"
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)
print(tup6)

# Accessing value in tuples
print(tup1[1])
print(tup2[1:])

# Add two tuples
tup7 = tup1 + tup2
print(tup1)
print(tup2)
print(tup7)

# convert a list into tuples
listConvert = [1, 2, 3]
newTuple = tuple(listConvert)
print(newTuple)