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

# Break, continue statements and else clauses on loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number: ", num)
        continue
    print("Found a number: ", num)

# Pass statements: is a null operation, nothing happen whe it executes
# Pass is useful in places where your code will eventually go, but have not been written yet.
for number in range(1,10):
    if number % 2 == 0:
        pass
        print("will be added code here")
    else:
        print("Found an odd number: ", number)
print("Out of loop")
