squares = [1, 4, 9, 16, 25]
print(squares)

# list can be indexed and sliced
print(squares[0])
print(squares[-1])
print(squares[-3:])

# all slice operations return a new list containing the requested elements
# return a new shallow copy of the list
print(squares[:])

# list also support operations like concatenation
print(squares + [26, 67, 98])

# list can be mutable
squares[0] = 3
print(squares)

# append() method to add new item regardless type at end of list
squares.append(28)
squares.append("string added")
squares.append(7 * 5)
print(squares)

# list can be updated using slices
squares[5:] = []
print(squares)

# built-in function len() also applies to list
print(len(squares))

# list can be nested
insideList1 = [1, 2, 3]
insideList2 = [4, 5, 6]
outsideList = [insideList1, insideList2]
print(outsideList)
print(outsideList[0])
print(outsideList[1])
print(outsideList[0], outsideList[1])

# delete list elements

del insideList1[1]
print(insideList1)

# list operation
# 1. Concatenation
newList1 = insideList1 + insideList2
print(insideList1)
print(insideList2)
print(newList1)
# 2. Reputation
newList2 = insideList1 *4
print(insideList1)
print(newList2)
# 3. Membership
print(3 in insideList1)
# 4. Iteration
for x in insideList2:
    print(x)

