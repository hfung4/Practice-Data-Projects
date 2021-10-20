# https://www.youtube.com/watch?v=3ohzBxoFHAY
# Dunder Methods


class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



## Introduction

# In this section, we focus on special methods that we can use within our classes.  Sometimes, these are
# called magic or dunder methods.
# Dunder methods allow us to do "operator overloading" and change built-in behaviour of Python functions:
print(1+2)  # sum
print('a'+'b') #concat

# Notice that the behaviour of + when we + two string together and when we + two numbers together is
# different

emp_1=Employee('Henry', 'Fung', 160000)

# If I print the object, it will return an address <__main__.Employee object at 0x1115191c0>. What if
# we want to change the behaviour of printing an object?  Instead of returning an address whenever I print an object,
# I might want to get some more useful information. As we will see, we can use dunder methods to help
# do that.
print(emp_1)

# __init__ is called "dunder init".  "Dunder" means surrounding with double underscores.
# __init__ itself is a dunder method.

# Let's look at other common dunder methods

## Common dunder methods:  __repr__()  and __str__()
# I can apply repr(emp1) and str(emp1)  [same as emp1.__repr__()  and emp1.__str__()]
# repr: representation of an object that is used for debugging and logging, meant to be seen by other developers
# str: readable representation of an object tht is meant for end-users

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # We need to at least have a repr method, repr method serves as a 'fallback' for str method.  If I run str(emp1), and if
    # __str__() does not exist in the Employee class, Python will search for  __repr__() in the Employee class and run it.
    def __repr__(self):
        # ROT: I should return a string that I can use to recreate the object
        return ("Employee('{}','{}','{}')".format(self.first, self.last, self.pay))

    def __str__(self):
        # More arbitrary, I can print out something useful and readable.
        return "{} - {}".format(self.fullname(), self.email)



emp_1 = Employee('Henry', 'Fung', 160000)

print(emp_1)  # runs __str__(), if not exist, then run __repr__()

print(repr(emp_1))  # in the background, Python does this:  print(emp1.__repr__())
print(str(emp_1))   # in the background, Python does this:  print(emp1.__str__())




## Less common Dunder methods
# Unless you are writing some complicated class, you will likely only use __init__(), __repr__(), and __str__() dunder methods.

print(1+2)  # in the background, Python is using a method in the integer class called "dunder add"
print(int.__add__(1,2))  # add the two integer objects

# Strings have their own dunder add method
print('a'+'b')
print(str.__add__('a','b')) # concat the two str objects

len('Henry') # number of char in string, or the length of the string list
# In the background
str.__len__('Henry')



# I can actually customize how addition works for our objects by creating our own dunder add methods
# Let's say, if we add the two Employee objects together, we want to compute the sum of the salary of the two Employees.

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        # ROT: I should return a string that I can use to recreate the object
        return ("Employee('{}','{}','{}')".format(self.first, self.last, self.pay))

    def __str__(self):
        # More arbitrary, I need to print out something useful and readable.
        return "{} - {}".format(self.fullname(), self.email)

    # My own dunder add method
    # self is instance from which I call __add__, other is another Employee object that I pass to __add__()
    def __add__(self, other):
        return self.pay + other.pay

    # customized dunder len method
    # return the length of the fullname string (number of char in fullname)
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Henry', 'Fung', 160000)
emp_2 = Employee('James', 'Wong', 40000)

# __add__
print(emp_1+emp_2)
# Same as
print(emp_1.__add__(emp_2))

# __len__
print(len(emp_1))
#Same as
print(emp_1.__len__())
