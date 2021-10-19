# https://www.youtube.com/watch?v=jCzT9XFZ5bw&t=2s

# We learn how to use the property decorator.

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return"{} {}".format(self.first, self.last)

# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

print(emp_1.first)  # Henry
print(emp_1.last) # Fung
print(emp_1.email) # Henry.Fung@gmail.com
print(emp_1.fullname()) #Henry Fung


# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

# What if I want to change the first name, can I do it like this?
emp_1.first = 'Jim'

print(emp_1.first)   #'Jim'
print(emp_1.last)    #'Fung'
print(emp_1.email)   #Henry.Fung@gmail.com   *INCORRECT*
print(emp_1.fullname())  # Jim Fung

# Two observations:
# 1) I change the first name to 'Jim' after I init emp_1 with 'Henry' as first name.
# The full name  is 'updated' since the full name method takes the current(updated) 'first' and 'last' attributes as input arg.

#2) The email is NOT updated since the email attribute is set within the constructor (email attribute is set during initialization)

# Solution: Can we just change the way email is set?
# Instead of setting email in the constructors,  We define a email method (like full name) that
# takes current first and last attributes as input args.

# PROBLEM:  Imagine I have many Employee objects in the code already.  I will need to go to every emp_1.email,
# emp_2.email, ..., emp_100.email and change it manually to emp_1.email(), emp_2.email()......

# In Python, we can use 'property decorators' that allow us to define a method that we can access like an attribute with no ()

## Property Decorators: Problem

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # define a new method called 'email'
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def fullname(self):
        return"{} {}".format(self.first, self.last)


# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

# What if I want to change the first name, can I do it like this?
emp_1.first = 'Jim'

print(emp_1.first)   #Jim
print(emp_1.last)    #Fung
print(emp_1.email())  # Need to add (), I need to manually do this whenever emp_x.email is used in the code **NO GOOD**
# print(emp_1.email) # Ideally, I want to instead continue to access the email method like an attribute with no ()
print(emp_1.fullname())  # Jim Fung


## Property Decorators: SOLUTION  @property


class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #property decorator
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def fullname(self):
        return"{} {}".format(self.first, self.last)


# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

# What if I want to change the first name, can I do it like this?
emp_1.first = 'Jim'

print(emp_1.first)   #Jim
print(emp_1.last)    #Fung
# print(emp_1.email())  # Need to add (), I need to manually do this whenever emp_x.email is used in the code NO GOOD
print(emp_1.email)  # no need () anymore since I add the property decorator on top of the email method in Employee class
print(emp_1.fullname())  # Jim Fung  (no @property, therefore I still need .fullname() instead of .fullname)

# KEY POINT:
# I define email() in the Employee class like a method
# But we access the email method like an attribute without the () because we use the property decorator.


## Property Decorators: apply this to the methods: fullname() and email() in the Employee class


class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #property decorator
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property  # property decorator
    def fullname(self):
        return"{} {}".format(self.first, self.last)


# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

# What if I want to change the first name, can I do it like this?
emp_1.first = 'Jim'

print(emp_1.first)   #Jim
print(emp_1.last)    #Fung
print(emp_1.email)  # no need () anymore since I add the property decorator on top of the email method in Employee class
print(emp_1.fullname)  # no need () anymore since I use property decorator


## Property Decorators: setters (PROBLEM)

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #property decorator
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property  # property decorator
    def fullname(self):
        return"{} {}".format(self.first, self.last)

# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

# Let's say I want to change the employee full name.  Instead of changing it like this:
emp_1.first ='Jim'
emp_1.last ='Wong'
print(emp_1.fullname) # Jim Wong

# I want to instead set fullname like this:
#emp_1.fullname = 'Jim Wong'

# And by doing this, I also want the first, last and email attributes to change automatically.



## Property Decorators: setters (SOLUTION)

class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #property decorator
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property  # property decorator
    def fullname(self):
        return"{} {}".format(self.first, self.last)

    # setter
    # syntax for setter is [name of property].setter
    # This is followed by a method [name of property]()
    # Purpose of fullname.setter is to change the first and last attributes
    @fullname.setter
    def fullname(self, name):   # the input arg 'name' is the new name we want to set fullname to.
        first, last = name.split(' ')  # split by space ' '
        self.first = first # set my first and last attributes to the new name
        self.last = last

# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

print(emp_1.first)   #Henry
print(emp_1.last)    #Fung
print(emp_1.email)   # Henry.Fung@gmail.com, use property decorators, no need .email()
print(emp_1.fullname)  # Henry Fung, use property decorators, no need .fullname()



# Old way:
#emp_1.first ='Jim'
#emp_1.last ='Wong'
# print(emp_1.fullname)

# New way: use setter to change the first and last attributes
emp_1.fullname = 'Jim Wong'  # KEY POINT: 'Jim Wong' goes to the 'name' input arg in the setter method

print(emp_1.first)   #Jim
print(emp_1.last)    #Wong
print(emp_1.email)   # Jim.Wong@gmail.com, use property decorators, no need .email()
print(emp_1.fullname)  # Jim Wong, use property decorators, no need .fullname()



## Property Decorators: deleters


class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #property decorator
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property  # property decorator
    def fullname(self):
        return"{} {}".format(self.first, self.last)

    # setter
    @fullname.setter
    def fullname(self, name):   # the input arg 'name' is the new name we want to set fullname to.
        first, last = name.split(' ')  # split by space ' '
        self.first = first # set my first and last attributes to the new name
        self.last = last

    # deleter: deletes the first and last attributes (set both attributes to None)
    @fullname.deleter
    def fullname(self):  # only accept self as input arg
        print('Delete Name')
        self.first= None
        self.last = None



# instantiate Employee class
emp_1 = Employee('Henry', 'Fung')

print(emp_1.first)   #Henry
print(emp_1.last)    #Fung
print(emp_1.email)   # Henry.Fung@gmail.com, use property decorators, no need .email()
print(emp_1.fullname)  # Henry Fung, use property decorators, no need .fullname()



# Use setter to change the first and last attributes
emp_1.fullname = 'Jim Wong'  # KEY POINT: 'Jim Wong' goes to the 'name' input arg in the setter method

print(emp_1.first)   #Jim
print(emp_1.last)    #Wong
print(emp_1.email)   # Jim.Wong@gmail.com, use property decorators, no need .email()
print(emp_1.fullname)  # Jim Wong, use property decorators, no need .fullname()


# Use deleter to set emp1.first and emp1.last to None
del emp_1.fullname  # the del command tells Python to run @deleter.fullname

print(emp_1.first)   #None
print(emp_1.last)    #None
print(emp_1.email)   # None.None@gmail.com, use property decorators, no need .email()
print(emp_1.fullname)  # None None, use property decorators, no need .fullname()
