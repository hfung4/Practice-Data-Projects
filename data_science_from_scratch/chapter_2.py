''' Chapter 2: Python Review'
- A tutorial on common tricks and tools I can use in Python
'''

# printing loops

'''
for i in [1,2,3,4,5]:
    print(i)

for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5]:
        print (j)
        print(i+j)
print("done logging!")
'''

#------------------------------------------------------------

# Use \ to continue line
x = 1+2+3 + \
  4
print(x)

#------------------------------------------------------------

# Import module that contain functions/constants for working with regular expressions
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

#------------------------------------------------------------

# If I only need a few specific values from a module, use "from [module] import...."
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

#------------------------------------------------------------

# Functions

def double(x):
    return x*2

print(double(2))

#------------------------------------------------------------

# Python functions are "first class", meaning I can:
    # Assign a function to a variable
    # Then pass the variable (that represents the function) as an
    # argument to another function!

def apply_to_one(fcn): # the argument fcn is itself a function!
    # calls the function fcn with1 as its argument
    return fcn(1)

# assign a function to a variable
double_var = double
x= apply_to_one(double_var)
print(x) # 2


#------------------------------------------------------------
# Lambda to create short and anonymous functions

y = apply_to_one(lambda x: x+4)
print(y) # 5

#------------------------------------------------------------

# Function parameters can be given default values
def my_print(message = "This is my default message!"):
    print (message)

my_print("hello") # hello
my_print("")
my_print() # default message


def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

print(full_name())
print(full_name("Henry", "Fung"))

#------------------------------------------------------------

# Strings

# Python uses \ to indicate special characters

tab_string = "\t" # represents the tab character
not_tab_sting = r"\t" # represents '\t'
print(tab_string + " " + not_tab_sting)

# Using three double quotes, I can create multi-line strings
multiline_string = """ This is the first line.
And this is the second line.
And this is the third line."""
print(multiline_string)

#------------------------------------------------------------

# f-strings provide a simple way to sub values into strings  (only available Python 3.6 or newer)

first_name = "Joel "
last_name = "Grus"

full_name = f"{first_name}{last_name}"
print(f"{first_name}{last_name}")

# Alternatively
print("{}{}".format(first_name, last_name))

#------------------------------------------------------------

# Exceptions

# When something is wrong, Python raises an exception.  If unhandled,
# exceptions will cause your program to crash. You can handle them using try and except.

try:
    print(0/0) # division by 0
except ZeroDivisionError:  # use except to "catch or handle" the exception that would have cause program to crash
    print("Cannot divide by zero!") # tell user no division by 0.  Only execute this if an exception is thrown (error is encountered)


#------------------------------------------------------------

# Lists

integers = [1,2,3]
hetro_list = ["a", 1, True]
list_of_lists = [integers, hetro_list]
print(list_of_lists)

list_length = len(integers) # 3
list_sum =  sum(integers) # 6

print(list_sum)

#------------------------------------------------------------

x = [0,1,2,3,4,5,6,7,8,9]

zero = x[0] # 0
nine = x[-1] # get first element from the right
seven = x[-3] # get third element from the right
print(seven)

# overwrite elements
x[0] = 22 # first number is now 22

#------------------------------------------------------------

# Slicing lists

print(x[:3]) # first 3 elements
print(x[3:]) # 3 to the end
print(x[1:5]) # [1,2,3,4]
print(x[-3:]) # [7,8,9]
print(x[1:-1]) # without first and last elements
copy_of_x = x[:] # [22,1,2,...9]

# ------------------------------------------------------------
[22,1,2,3,4,5,6,7,8,9]

# Every three elements
print(x[::3]) # [22,3,6,9]
print(x[1:6:2])  # [1,3,5]    [start:end:step]
print(x[5:2:-1])  # start is 5, end is 2, step is -1 [5,4,3]

# --------------------------------------------------------------

# Use "in" to check if an integer is a member of a list
# Check each element one at a time, so use this only if you know the list is small
1 in [1,2,3] # True
0 in [1,2,3] # False

# ----------------------------------------------------------------

# Add elements to a list

# Modify a list in place
x = [1,2,3]
x.extend([4,5,6])  # append 4,5,6 to the end of the list
print(x)  #[1,2,3,4,5,6]

y = x+[4,5,6] # y is [1,2,3,4,5,6], x is unchanged

for i in (11,22,33):
    x.append(i)
print(x)


# ----------------------------------------------------------------

# If I know how many elements there are in a list, I can unpack it
x,y = [1,2] # x=1, y=2

# If I don't care about 1, I can use a _ as a placeholder for the value you are going to throw away

_,y=[1,2]

print(y)

# ----------------------------------------------------------------

# Tuples

# Tuples are immutable lists. EVERYTHING that you do to a list, you can do witih tuples, EXCEPT you cannot modify them
my_list= [1,2]
my_tuple = (1,2)

print(my_list)
print(my_tuple)

# change an element in my_list
my_list[1] = 200
print(my_list)

# try to do the same with tuples
try:
    my_tuple[1] = 200
except TypeError:
    print("Cannot modify a tuple!")


# One use of tuples is that they can return multiple values from functions

def sum_and_products(x,y):
    _sum = x+y
    _product = x*y
    return _sum,_product

print(sum_and_products(2,3))  # (5,6)

s,p = sum_and_products(5,10)  # s is 15, p is 50

# Both tuples and lists can be used for multiple assignments

x,y = 1,2
x,y = y,x  # swap variables.  x gets y's value, y gets x's value