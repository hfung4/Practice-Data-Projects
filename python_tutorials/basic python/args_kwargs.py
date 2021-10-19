## The use of *args and **kwargs in Python functions


# The use of *args
# *args (can also be *vars, *inputs .....) represents a variable number of arguments in a
# a function.  For example, if I have a function f(x), but I want x to represent any number of inputs, then
# I can use f(*args)

# Example
def variable_args_fcn(normal_input, *args):
    print("The first normal argument is {}".format(normal_input))

    # arg is treated like an array in the function
    for i in args: # no more *args, instead use args
        print ("Another function arguments is: {}".format(i))

# Test the function
variable_args_fcn("my normal input", "steak", "lobster", "ice-cream", "ribs")

# I can define a tuple

myVec=(1,99,3,11)
variable_args_fcn(55, *myVec)  # If I use tuple as input, need to use *myVec to indicate that it is a tuple


## The use of **kwargs
# **kwargs (can also be **vars, **inputs .....) represents a "key-worded" variable number of arguments of a function
# I want to use **kwargs if you want to handle "named arguments" in a function.  **kwargs is like a named vector
# Input arguments **kwargs have two parts: 1)key, and 2) value.  In the function, kwargs is treated like a dictionary/named vector.

def greet_me(**kwargs):
    if kwargs is not None:  # named vector is not empty
        for key, value in kwargs.items():  # I can use .item() to access the elements of a named vector
            print("The key is {}, and the value is {}".format(key, value))

greet_me(Name="Henry", Age=33, Sex="Male")
            

# Second example
def print_keyword_args(**kwargs):
     for key, value in kwargs.items():
        print ("{}:{}".format(key, value))
        
print_keyword_args(first_name="John", last_name="Doe")

# I can define an input dictionary and use it as input
myDict={'first_name': 'Henry', 'last_name': 'Fung', 'Age': 33, 'Sex':'Male'}

print_keyword_args(**myDict)  # if I use a dict as input, I need the two ** to indicate myDict is a dictionary

# Third example
def test(**kwargs):
    print(kwargs['a']) # access the named vector by its keys. a,b, and c are the keys of the named vector
    print (kwargs['b'])
    print (kwargs['c'])

myDict = {'a': 1, 'b': 2, 'c': 3}
print(myDict['b'])

test(**myDict)  # if I use a dict as input, I need the two ** to indicate myDict is a dictionary

# Fourth example

# Since **kwargs encompasses in one or more named vectors arguments, I can do the following
def test2(**kwargs):
    for key, value in kwargs.items():
        print("The key is {} and the value is {}".format(key, value))

myDict = {'b': 2, 'c': 3}
test2(a=1,**myDict)  # if I use a dict as input, I need the two ** to indicate myDict is a dictionary



myDict1 = {'a': 1, 'b': 2, 'c': 3}
myDict2 = {'d': 4, 'e': 5, 'f': 6}
test2(**myDict1, **myDict2)



myDict1 = {'a': 1, 'b': 2, 'c': 3}
myDict2 = {'d': 4, 'e': 5, 'f': 6}
test2(g=7, h=8, **myDict1, **myDict2)




## I can also use *args in my function call (but not in my function defition)

def test(input1, input2, input3):  # Didn't use *arg or **kwargs in function definition!
    print("First Argument:", input1)
    print("Second Argument:", input2)
    print("Third Argument:", input3)


myArgs = ("two", 999, 1234)  # define a 3-tuple of input arguments
test(*myArgs)

# test(2, *myArgs) # ERROR, since my function only expects 3 arguments but I give 4

myArgs = (111, 999)  # define a 3-tuple of input arguments
test("Henry", *myArgs)

