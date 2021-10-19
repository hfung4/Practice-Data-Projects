# https://www.youtube.com/watch?v=RSl87lqOXDE

# 'Inheritance' is a functionality that allow us to create a class that inherits attributes and methods from a parent (base) class
# This is useful because we can create 'sub-classes' that inherits all the functionalities of a parent (base) class.  Then we can add
# new functionalities/modify some of the existing methods without affecting the parent (base) class in any way.

# Let's say we want to be a bit more specific and create different types (sub-classes) of Employees: Developers and Managers.
# Both Developers and Managers are going to have names, pay, and emails.  These are attributes that already exist in
# the Employee class.  So we don't need to define a new Developer class by copying a bunch of code from the Employee class.
# Instead, we can inherit these attributes (and/or methods) from the Employee class.


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


## Developer sub-class

# for a subclass, we need (), within the () we specify which class we want to inherit from
class Developer(Employee):
    pass

# Even without any code of its own, the Developer subclass will have all the attributes and methods from the Employee class

dev_1=Developer('Henry', 'Fung', 160000)
dev_2=Developer('James', 'Wong', 60000)

print(dev_1.email)
print(dev_2.email)

# Under the hood, when we instantiate the Developer class, Python first look in Developer blueprint to see
# if there are any __init__ methods.  Since Python does not find __init__(), it searches __init__() in the parent class.
# Python will "walk" up the chain of inheritance until it finds the attribute/method.  This chain of inheritance is called
# the 'method resolution order'.

# Get more info about the Developer class
print(help(Developer))
# One of the first thing that gets printed out is the method resolution order.
# These are the classes where Python searches for attributes/methods
# The order is: Developer--->Employee --> builtin object (parent class of every class in I create in Python)

# Second, I see a list of all methods in Developer that is inherited from Employee
# Third, I see a list of attributes inherited from Employee.  The class attribute 'raise_amount' in Devleoper is inherited
# from Employee



## New features for the Developer sub-class (customization of the parent class)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Let's say we want developers to have raise of 10%
class Developer(Employee):
    raise_amount=1.10

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)  # 10% raise

emp_1=Employee('John', 'Doe', 160000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)  # 4% raise, Employee class is not affected.



## Initialize the Developer sub-class with more inputs(info) than the parent class

# Suppose when we init the Developer class, we also want to pass in 'programming language' as an attribute

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):

        # Don't copy and paste code that handles first, last, pay.
        # Instead, let the init method in Employee class to "handle" first, last, pay.
        # Call parent init method:
        super().__init__(first,last,pay)  # super().__init__() is same as Employee.__init__()
        # Employee.__init__(self, first, last, pay)  also works, but not recommended

        # Use developer init method to handle prog_lang
        self.prog_lang = prog_lang

# When we pass in our input arguemnts, Python first runs the init method from the Employee class
# and set the first, last, and pay attributes.
# Then it runs the init method from the Developer class and sets the prog_lang attribute.
dev_1=Developer('Henry', 'Fung', 160000, 'Python')
dev_2=Developer('Joe', 'Wong', 50000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)



## The Manager subclass
# This class inherits all attributes and methods from the Employee class, plus it also has an attribute 'employees'
# that contains all employees that work under this manager.  This attribute is a list of Employee objects!

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):  # by default, the attribute employees is None (empty list)
        super().__init__(first, last, pay) # let init function from the Employee class to handle first, last, and pay

        if employees is None:
            self.employees = []  # if list of Employees objects is not provided to the class during instantiation
        else:
            self.employees = employees


    # A new method for the Manager class that adds new employees (Employee object) to employees
    def add_emp(self, emp):  # emp is an Employee object
        if emp not in self.employees:
            self.employees.append(emp)

    # A new method for the Manager class that removes Employee object from employees
    def remove_emp(self, emp): # emp is an Employee object
        if emp in self.employees:
            self.employees.remove(emp)

    # A new method for the Manager class that print out the list of Employee objects (full name) that the Manager supervises
    def print_emp(self):
        for e in self.employees:
            print('---->', e.fullname())  # call the fullname method of each Employee object in the list

#create new Manager object
mgr_1 = Manager('Jane', 'Smith', 90000, [dev_1, dev_2])  #employees is a list of Employee objects

print(mgr_1.email)

# print list of employee (fullname)
mgr_1.print_emp()

# remove Joe Wong
mgr_1.remove_emp(dev_2)
mgr_1.print_emp()

mgr_1.add_emp(dev_2)
mgr_1.print_emp()


## Useful built-in Python function: isinstance() and issubclass()

# isinstance: tells us if an object is an instance of a class
print(isinstance(mgr_1,Manager)) # True
print(isinstance(mgr_1,Employee)) # True, since mgr_1 is an instance of Manager, which itself is a subclass of Employee
print(isinstance(mgr_1,Developer)) # False

# issubclass: tells us if a class is a subclass of another
print(issubclass(Developer, Employee))  # Is Developer a subclass of Employee?  True
print(issubclass(Manager, Employee))  # Is Manager a subclass of Employee?  True
print(issubclass(Employee, Manager))  # Is Employee a subclass of Manager?  False
print(issubclass(Manager, Developer))  # Is Manager a subclass of Developer?  False

