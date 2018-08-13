print('D:\some\name')
# using raw strings if don't want characters prefaced by \
print(r'D:\some\name')


# string literals can span multiple line using '''...''' or """..."""
print("""\
Drink: add ons [OPTIONS]

       1. Rainbow jelly
       2. Honey boba
       3. Golden boba
""")

# string len

text = "testing len of a string"

print(len(text))


# accessing value in strings
var1 = 'Hello World'
var2 = 'Python Programing'

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])


# update string

print("updated string: ", var1[:6] + 'Python')

# string format operator

print("My car is %s and it is %d model!" % ('Toyota', 2015))

# unicode string

print(u"Hello,World")
