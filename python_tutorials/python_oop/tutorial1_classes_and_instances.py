# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

# A class has methods and attributes
# For example, we can make a class (blueprint) that represents an employee.
# Attributes include name, pay, email etc...

# A Class is a blueprint of creating instances
class Employee1:
    pass

# instance variables contain data that is UNIQUE to each instance
emp_1 = Employee1()
emp_2 = Employee1()

print(emp_1)  # have different memory addresses
print(emp_2)

## Manually set attributes to employee instances

# employee 1 instance attributes
emp_1.first = 'Henry'
emp_1.last = 'Fung'
emp_1.email = 'hfung4@jhu.edu'
emp_1.pay = '160000'


# employee 2 instance attributes
emp_2.first = 'James'
emp_2.last = 'Wong'
emp_2.email = 'jwong@jhu.edu'
emp2_pay = '10000'

print(emp_1.email)
print(emp_2.email)


##  __init__ function   (constructor)
# Allow attributes of an instance to be initialized at the creation of an instance

class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'


emp_1=Employee('Henry', 'Fung', 160000) # instance is passed to the __init__ function automatically, so no need to pass 'self'
emp_2=Employee('James', 'Wong', 60000)


print(emp_1.email)
print(emp_2.email)


##  For an instance to 'perform some action', I need to define some methods for the class


class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # 'self.first ='  is same as  'emp1.first ='
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):  # take instance as argument, ALWAYS need self as argument
       return "{} {}".format(self.first, self.last)


emp_1=Employee('Henry', 'Fung', 160000) # instance is passed to the __init__ function automatically, so no need to pass 'self'
emp_2=Employee('James', 'Wong', 60000)

# emp_1 is autonmatically passed to the fullname() method.  So we need to have a self arg to 'catch' that
print(emp_1.fullname())
print(emp_2.fullname())

# run it from the class itself
print(Employee.fullname(emp_1)) # need to pass instance manually
print(emp_1.fullname())

# In the background, this is actually what happens if I run emp_1.fullname(), Python
# will run method directly from the class, and then pass emp_1 as the first arg

