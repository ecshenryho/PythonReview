# functions reviews
# 1. Function declaration, function call
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')  # escape original end line to have them print in 1 line
        a, b = b, a + b
    print("\na > n, out of loop")
    return


fib(15)  # expected 2 blank lines after class or function definition
print(fib(5))


def fib2(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)  # escape original end line to have them print in 1 line
        a, b = b, a + b
    return result  # Return statement


resultCallFib = fib2(15)  # function call statement
print(resultCallFib)

# 2. Pass by value vs pass by reference. All parameters (arguments) in python passed by reference


def increment(a):
    a += 1
    print("value of a inside function: ", a)
    return


a = 9
increment(a)  # change the value of a
print("value of a outside function: ", a)  # not print out 10,
# because we can not pass a simple primitive by reference in python
# it works with list


def modify(list):
    list.append([1, 2, 3])
    print("value of a inside list: ", list)
    return


list = [0, ]
modify(list)
print("value of a outside list: ", list)  # they list being modified and print out the same list

# 3. Default arguments


def sum(a = 1, b = 1):
    c = a + b
    if a == 1 and b == 1:
        print("default values was used.")
    else:
        print("the sum is: ", c)


num1 = 3
num2 = 5
num3 = 0
sum(num1, num2)  # print out 8
sum(num1, )  # print out 4

# 4. keyword arguments
# keywords can be used to match the values with parameters


def print_function(str):
    print(str)
    return


print_function(str="this is a string")


# 5. Variable-length arguments
# process a function for more arguments than specified while defining it


def print_info(argument1, *var_tuple):  # * is placed to hold the values of all non-keyword variable arguments
    print("output is: ")
    print(argument1)
    for n in var_tuple:
        print(n)
    return


print_info(10)
print_info(10, 20, 30)


# 6. keyword arguments


def greet(name, message="good morning"):
    print("Hello", name + ', ' + message)


greet("Henry")
greet("Henry", "How are you doing?")
greet(name="Anna", message="How do you do?")  # call function using keyword argument
greet("Henry", message="what are you doing?")

# 7. arbitrary arguments
# don't need to know in advanced the number of arguments that will be passed


def greet2(*list_name):  # an asterisk to denote this type of argument.
    for name in list_name:
        print("Hello", name)


greet2("Henry", "Anna", "Katie")
