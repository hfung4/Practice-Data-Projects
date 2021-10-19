# https://www.youtube.com/watch?v=BJ-VvGyQxho

# instance variables are variables that are UNIQUE to each instance.
# For example, first, last, pay, and email are different for each instance.
# They are the data for each employee.
# So far, we used the init function to set instance variables at the time of creation of
# an instance

# In this tutorial, we focus on 'class variables'.  Unlike 'instance variables',
# class variables are NOT unique for each instance (employee); rather, they
# are shared amongst ALL employees (instances).

# Company gives the SAME annual salary raises for every employee (a constant).
# So we can define a class variable for that.  This class variable would be the same for
# all employees.

## 1  Intro to class variables

class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(
            self.pay * Employee.raise_amount)  # set this as an integer so it will be casted as a whole number
        # I can access a class variable from both the class itself, or from the instances
        # self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Henry', 'Fung', 50000)
emp_2 = Employee('James', 'Wong', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# I want to access the raise amount, as well as update the raise amount for ALL employees
# When I access a class variable through an instance, Python will first check if raise_amount is
# a instance variable (attribute), if NOT, then it will check if raise_amount is a class variable,
# or whether raise_amount is an attribute from an inherited class.

# emp_1 instnace doesn't actually have the raise_amount attribute, rather it access the class attribute
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# Since raise_amount is a class variable (apply to ALL instances), we should be able to access directly from class:
print(Employee.raise_amount)


## 2 Namespace of class vs Namespace of instance when class variable is created

class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(
            self.pay * Employee.raise_amount)  # set this as an integer so it will be casted as a whole number
        # I can access a class variable from both the class itself, or from the instnaces
        # self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Henry', 'Fung', 50000)
emp_2 = Employee('James', 'Wong', 60000)

# I can try to print out the 'namespace' of emp_1
print(emp_1.__dict__)

# I get {'last': 'Fung', 'email': 'Henry.Fung@company.com', 'first': 'Henry', 'pay': 50000}
# if I were to access the last, email, pay etc..., these are the values that I would get from emp_1.X
# but notice there is no 'raise_amount' in the list since it is a class variable

print(Employee.__dict__)  # namespace of Employee does contain raise_amount attribute


## 3 Updating and changing class variables; creating new instance variables


class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(
            self.pay * Employee.raise_amount)  # set this as an integer so it will be casted as a whole number
        # I can access a class variable from both the class itself, or from the instnaces
        # self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Henry', 'Fung', 50000)
emp_2 = Employee('James', 'Wong', 60000)

Employee.raise_amount = 1.05  # change the class variable

# changes to 1.05 for the class and all the instances
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# if I attmept to change raise_amount from instance, I WON"T change the class variable 'raise_amount'.
# Rather, since 'raise_amount" is not an instance variable of emp1, Python will think that the user wants
# to create a new instance variable called 'raise_amount' for emp_1
emp_1.raise_amount = 1.01

print(emp_1.__dict__)  # has raise_amount in emp_1 namespace
print(emp_2.__dict__)  # no raise_amount in emp_2 namespace

# Only the raise_amount variable for emp_1 changes to 1.01
# the reason is that when I made the 1.01 assignment, I actually
# CREATED a raise_amount attribute for the instance emp_1.  So now
# There are now two 'raise_amount'. One is associated with the class Employee and
# another is associated with the instance

# Since emp_1 has raise_amount in its namespace, when I access raise_amount in emp_1,
# Python will first check to see if it is an instance attribute (which it is now), and thus
# it will print out the value of the instance attribute (1.01), rather than the class attribute (1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)


# ROT:
# In the apply_raise method, rather than using  'Employee.raise_amount"
# self.pay = int(self.pay * Employee.raise_amount)  # set this as an integer so it will be casted as a whole number

# I can use:
# self.pay = int(self.pay * self.raise_amount) so that if I want to change the raise_amount for only an instance, I can.
# ie: If I 'create' a new instance variable 'raise_amount', the function will use it instead of the class variable 'raise_amount'.


## 4:  Another class variable

# Another class variable is the number of employees in the company
# This number should be the same for all employees


class Employee:
    # Class variables
    raise_amount = 1.04  # a constant that applies to all instances, no need 'self'
    num_of_emps = 0  # number of employees, I can updagte this class variablein __init__ everytime a new instance is created

    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # change attribute from the class itself (Employee.num_of_emps), since there is no use case for
        # us to have different num_of_emps for different employees (unlike raise_amount)
        Employee.num_of_emps += 1  # increment by 1

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # set this as an integer so it will be casted as a whole number


emp_1 = Employee('Henry', 'Fung', 50000)
emp_2 = Employee('James', 'Wong', 60000)

# incremented twise when we instantiated two employees, so I get 2
print(Employee.num_of_emps)  # 2


# NOTE: there are 'class/static methods' (similar to class variable) that we can define.  Will talk about it in future
# tutorials.
