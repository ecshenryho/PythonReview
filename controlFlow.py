# if statement
x = int(input("Please enter an integer: "))
if x < 0:
    print("It is a negative number.")
elif x == 0:
    print("It is a Zero")
else:
    print("It is a positive number")

# for statement
list1 = [-1, 2, 3]

for i in list1:  # Print all elements in list
    print(i)

if all(j > 0 for j in list1):  # check it contains negative values
    print("List of positive elements")
else:
    print("List has negative values")

# The range() function
for i in range(2):
    print(list1[i])
print(list(range(0)))
print(list(range(10)))
print(list(range(1, 10)))

start = 0
stop = 14
step = 2
print(list(range(start, stop, step)))

x = range(6)
for n in x:
    print(n)
