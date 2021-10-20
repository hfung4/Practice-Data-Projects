# https://www.youtube.com/watch?v=rq8cL2XMM5M

# We will study three kinds of methods:  1) regular methods, 2) class methods, and 3) static methods.

# Regular methods in a class automatically takes instance as the first arg. So we need "self" when
# we define regular methods in a class to "catch" the instance arg.
# What if we want to change that:  instead we want a method to automatically take a class as the first input arg.
# In this case, this method is called a "class method".
# To do this, we need to use a decorator @classmethod, and then define the class method

# Why we want to do that?
# We want to write a "class method" that changes a class variable raise_amount.
# If I don't do that, and instead use create a function that have the line self.raise_amount = 1.09 (same as emp1.raise_amount)
# Then Python will just create a new instance variable for emp1 with the same name "raise_amount'
# And emp1 will have a different raise_amount than emp2 (since Python checks if "raise_amount" is an instance variable first
# before checking if it is a class varaible".

class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'
    num_of_emps = 0  # number of employees, I can updagte this class variablein __init__ everytime a new instance is created

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  # increment by 1

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # set this as an integer so it will be casted as a whole number

    # classmethod decorator, this decorator "alters" the functionality of a method: where it will now
    # receive class as the first arg instead of the instance.  By convention, we call class arg as "cls"
    @classmethod
    def set_raise_amt(cls,amount):  # in the set_raise_amt method we now work with a class rather than an instance
        cls.raise_amount = amount  # same as Employee.raise_amount = amount


emp_1 = Employee('Henry', 'Fung', 50000)
emp_2 = Employee('James', 'Wong', 60000)


print(Employee.raise_amount)  #1.04 , the initial value of the class variable raise_amount
print(emp_1.raise_amount)  #1.04
print(emp_2.raise_amount) #1.04

# Let's change the class variable raise_amount to 1.05 using the class method
Employee.set_raise_amt(1.05) # Employee class is automatically passed to function as first arg
# NOTE: I run classmethod from class Employee.set_raise_amt(1.05) instead of from instances emp1.set_raise_amt(1.05)
# No one ever run classmethod from the instance, although it still works, it makes no conceptual sense.


## classmethods as alternative constructors

# classmethods can be alternative constructors.  You can use classemethods to make multiple ways
# to create the object (for specific use-cases).

# Let's say I want to use the below three strings as inputs to create a new Employee instance.
# The first name, last name, and salary are all in a string that is separated by '-'

str_1='John-Doe-70000'
str_2='Steve-Smith-30000'
str_3='Jane-Doe-90000'

# The 'dumb' way
first, last, pay = str_1.split('-')  # split string by '-'
new_emp_1 = Employee(first, last, int(pay)) # use the resulting values to init an Employee instance

print(new_emp_1.pay)
print(new_emp_1.email)


# The fast way (create an alternative constructor that allow user to pass in string as input to the constructor)


class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'
    num_of_emps = 0  # number of employees, I can updagte this class variablein __init__ everytime a new instance is created

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  # increment by 1

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # set this as an integer so it will be casted as a whole number

    # classmethod decorator, this decorator "alters" the functionality of the method where it will now
    # receives class as the first arg instead of the instance.  By convention, we call class arg as "cls"
    @classmethod
    def set_raise_amt(cls,amount):  # within the set_raise_amt method, we now work with a class rather than an instance
        cls.raise_amount = amount  # same as Employee.raise_amount = amount

    # Alternative constructor called 'from_string'
    @classmethod
    def from_string(cls,emp_str): # takes in class as first arg, and emp_str as second arg
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # create and return Employee object
    # Create new employee instance
    # cls(first, last, pay) is equivalent to Employee(first, last, pay)- the way we usually
    # instantiate our class. For example: emp_1=Employee('Henry', 'Fung', 160000)
    # need to return newly created Employee object so that user can receive the Employee object when from_string() is called


str_1='John-Doe-70000'
str_2='Steve-Smith-30000'
str_3='Jane-Doe-90000'

# create a new Employee object using string inputs by calling the class function 'from_string'
new_emp_1=Employee.from_string(str_1)   # class methods are ALWAYS called from class

print(new_emp_1.pay)
print(new_emp_1.email)


## Static methods

# When working with classes:
    # regular methods automatically pass instances as the first arg  (use 'self' to catch that)
    # class methods automatically pass class as the first arg (use 'cls' to catch that)
    # static methods do not pass anything automatically as the first arg.


# Static methods are just like normal functions, but they are defined within a class because they have some
# logical connection/relation with the class.

# Suppose we have a simple function that takes in a day, and returns a boolean that tells me if it is a workday or not.
# Such a function has a logical to our Employee class, but it doesn't need any Class or Instances variables.

# To create a static method, we use the @staticmethod decorator

# The biggest indicator that a method is 'static' is if the method doesn't access instance or class variable
# anywhere within the function.


class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'
    num_of_emps = 0  # number of employees, I can updagte this class variablein __init__ everytime a new instance is created

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  # increment by 1

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # set this as an integer so it will be casted as a whole number

    # classmethod declarator, this declarator "alters" the functionality of the method where it will now
    # receives class as the first arg instead of the instance.  By convention, we call class arg as "cls"
    @classmethod
    def set_raise_amt(cls,amount):  # within the set_raise_amt method, we now work with a class rather than an instance
        cls.raise_amount = amount  # same as Employee.raise_amount = amount

    # Alternative constructor
    @classmethod
    def from_string(cls,emp_str): # takes in class as first arg, and emp_str as second arg
        first, last, pay = emp_str.split('-')
        # Create new employee instance
        # cls(first, last, pay) is equivalent to Employee(first, last, pay), the way we usually instantiate our class
        # need to return newly created Employee instance so that user can receive the Employee object when this function is called
        return cls(first, last, pay)  # return the newly created Employee object


    @staticmethod
    def is_workday(day):  # no self of cls arg, no interaction with any attributes or methods in the
        # Employee class!
        # sat or sun, use Python build-in function weekday(), assuming that "day" is a Python datetime variable
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2016,7,10)

# use static method to check if date is a 'weekday'
# NOTE: I call static method from Employee class
print(Employee.is_workday(my_date)) # False

# create new instance using the alternative constructor
emp_str_1='John-Doe-70000'
new_emp_1=Employee.from_string(emp_str_1)


# call static method from instance
print(new_emp_1.is_workday(my_date))  # False, also works!