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

# If I only need a few specific values from a module, use "from [module] import X, Y ...."
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

def apply_to_one(f): # the argument fcn is itself a function!
    # calls the function fcn with 1 as its argument
    return f(1)

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
my_print() # default message

# specify the names of the arguments.
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
print("{} {}".format(first_name, last_name))

#------------------------------------------------------------

# Exceptions

# When something is wrong, Python raises an exception.  If "unhandled", exceptions will cause
# your program to crash. You can handle them using try and except.

try:
    print(0/0) # division by 0
except ZeroDivisionError:  # use except to "catch or handle" the exception that would have cause program to crash
    # tell user no division by 0.  Only execute this if an exception is thrown (error is encountered)
    print("Cannot divide by zero!")


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

print(x[:3]) # first 3 elements  index 0,1,2
print(x[3:]) # index 3 to the end
print(x[1:5]) # [1,2,3,4]  include index 1, exclude index 5
print(x[-3:]) # [7,8,9]
print(x[1:-1]) # without first and last elements
copy_of_x = x[:] # [22,1,2,...9]

# ------------------------------------------------------------
x= [22,1,2,3,4,5,6,7,8,9]

# Every three elements
print(x[::3]) # [22,3,6,9]
print(x[1:6:2])  # [1,3,5]    [start:end:step]
print(x[5:2:-1])  # start is index 5 (inclusive), end is index 2 (exclusive), step is -1 [5,4,3]

# --------------------------------------------------------------

# Use "in" to check if an integer is a member of a list
# Check each element one at a time, so use this only if you know the list is small
1 in [1,2,3] # True
0 in [1,2,3] # False

# ----------------------------------------------------------------

# Add elements to a list

# Modify a list in place
x = [1,2,3]
x.extend([4,5,6])  # append 4,5,6 to the end of the list  (in place)
print(x)  #[1,2,3,4,5,6]

x + [4,5,6] # not in place

y = x+[4,5,6] # y is [1,2,3,4,5,6], x is unchanged

for i in (11,22,33):
    x.append(i) # in place
print(x)


# ----------------------------------------------------------------

# If I know how many elements there are in a list, I can unpack it
x,y = [1,2] # x=1, y=2

# If I don't care about 1, I can use a _ as a placeholder for the value you are going to throw away
# I can print _ and will get 1.  So the use of _ as a placeholder is only an convention.

_,y=[1,2]

print(y)

# ----------------------------------------------------------------

# Tuples

# Tuples are immutable lists. EVERYTHING that you do to a list, you can do with tuples, EXCEPT you cannot modify them
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


# ----------------------------------------------------------------

# Dictionaries

# Dictionaries associate values with keys. I can retrieve a value in a dict with its corresponding key.
# Dictionary keys must be “hashable”; in particular, you cannot use lists as keys.


empty_dict = {}
grades = {"Henry":99,
          "John": 80}

henry_grade = grades["Henry"] # 99

# I get a KeyError if I ask for a key that is not in the dict.
try:
    jen_grade = grades["Jen"]
except KeyError:
    print("No grade for this person")

# To avoid this issue, I should check for the existance of a key in a dict.
# Membership checks are fast even in large dicts
henry_has_grade = "Henry" in grades # True
jen_has_grade = "Jen" in grades # False

99 in grades # the "in" clause only checks for keys in dicts

# Another example for this:
x = [1,2,3]
3 in x # True

x = {"henry":1, "john":2, "kate":3}
3 in x # False
"kate" in x # True


# get method for dictionaries
# I can use dict.get() to retrieve a value from a dict based on key.
# If the key does not exist, you will get a user-specified default value rather than a KeyError

henry_grade = grades.get("Henry", 0) # 0 is the default value if "henry" DNE in the dict
john_grade = grades.get("John", 0)

jen_grade = grades.get("Jen", 0) # 0
jen_grade = grades.get("Jen", -1) # -1
jen_grade = grades.get("Jen") # None

# I can assign value to a key
grades["Henry"] = 100
grades["John"] = 70
print(grades)

# I can add elements in a dict
grades["Exor"] = 1000
print(grades)

# Just like lists and tuples, I can find length of dict using len()
x = [1,2,3]
print(len(x))

x = {1,2,3}
print(len(x))

print(len(grades))

# I can have a mix of datatypes within a dict
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print(tweet)

# I can print out ALL the keys
print(tweet.keys())
# I can print out all the values
print(tweet.values())

# I can use .item() to get an iterable of (key,values) tuples
tweet_items = tweet.items()
print(tweet_items)

for k,v in tweet.items():
    print(f"The key is {k}, and the value is {v} \n")

# To check for membership of a key in a dict, use the following
"tweet_length" in tweet # False

# And not:
"tweet_length" in tweet.keys()

# To check for a value in a dict (slow but the only way to check)
1000 in grades.values()


## Defaultdict

# Suppose you have a document and you want to count the freq of each vocab
doc = ["henry", "is" , "a" , "data", "data", "scientist", "scientist", "scientist",
       "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]

# One approach is to create a dict in which the keys are the vocab and the value are the count.
# If the word DNE in the dict, I add it to the dict.  I increment the count of each word if it exists already
# in the dict.

word_counts = {} # init the dict
for word in doc:
    if word in word_counts:
        word_counts[word] +=1
    else:
        word_counts[word] = 1

print(word_counts)

# I can implement the same thing by using try and exception.
# If the word DNE in the dictionary, I handle the exception by
# adding it to the dict.

word_counts = {} # init the dict
for word in doc:
    try:
        word_counts[word] +=1
    except KeyError:
        word_counts[word] =1

print(word_counts)


# The third approach uses .get()
word_counts = {} # init the dict
for word in doc:
    # save the previous count (the count before my dict update, if word DNE, then default its value to 0).
    previous_count = word_counts.get(word,0)
    # update dict
    word_counts[word] = previous_count + 1

print(word_counts)


# ***** NEW APPROACH: defaultdict ********
# A defaultdict is like a regular dictionary, except that when you try
# # to look up a key it doesn’t contain, it first adds a value for it using
# # a "zero-argument function" you provided when you created the defaultdict.


# Suppose you have a document and you want to count the freq of each vocab
from collections import defaultdict

word_counts = defaultdict(int) # int() produces 0
for word in doc:
    word_counts[word] +=1

print(word_counts)


# Defaultdicts are also useful with list of dict, or even your own functions

dd_list = defaultdict(list) # list() produces an empty list
dd_list["Lucy"].append(5)
print(dd_list)  # The new key Lucy is associated with a list with element 5  {'Lucy': [5]}

dd_dict = defaultdict(dict) # dict() produces an empty dict
dd_dict["Henry"]["my_key"] = "my_val"
# The new key "Henry" is associated with a dict element, with "my_key" as its key and "my_val" as its value
print(dd_dict) # A dict of dicts

dd_pair = defaultdict(lambda: [0,0]) # define a function that outputs [0,0] for every new key
dd_pair["John"][1] = 44  # change the second element to 1
print(dd_pair)  # {'John': [0, 44]})


# These defaultdicts will be useful when we’re using dictionaries to “collect”
# results by some key and don’t want to have to check every time to see if the key exists yet.


## Counters

# A counter turns a sequence of values into a defaultdict(int)- like object mapping keys to counts

from collections import Counter
c = Counter([0,1,2,0])
print(c) # Counter({0: 2, 1: 1, 2: 1})

# I can use Counter to solve our word_counts problem
doc = ["henry", "is" , "a" , "data", "data", "scientist", "scientist", "scientist",
       "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]
word_counts = Counter(doc)
print(word_counts) # word_counts is a dict of each vocab in the doc (key) and the count of each word (val)

word_counts.most_common(3) # To get the most common three word, use the most_common() function of the Counter instance

for word, count in word_counts.most_common(3):
    print(word, count)


## Sets
# Set is another useful data structure. It represents a collection of distinct items.
# The difference between Tuples and Sets:
    # Tuples are EXACTLY like a list, except you can't modify them
    # Tuples can have "repeated" elements (7,7)
    # Tuples are used in case we want to output 2 or more variables from a function.

    # Sets only contains unique elements
    # "in" clause works very fast on sets.
    # If we have a large collection of items that we want to use for a membership set, use set rather than list.
    # Use set to find a collection of distinct items in a collection.

primes_below_10 = {2,3,5,7}
empty_set = set() # don't use {}

s = set() # init an empty set
s.add(1) # inplace add an element to the set
s.add(2)  # {1,2}
s.add(2) # still {1,2} since set only contains unique elements

print(len(s)) # 2
2 in s # True
3 in s # False

# Use set to check membership of an item in a very large collection of items
# stopwords_set = set(stopwords_list)
# "zip" in stopwords_set      # very fast to check

# Use set to find distinct items in a collection
item_list = [1,2,3,1,2,3]
num_items = len(item_list) # 6
item_set = set(item_list) # convert list to set
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set)  #[1,2,3]
print(distinct_item_list)


## Control flow

# if....elif....else
x = 10

if x > 2:
    print ("Greater than 2")
elif x > 3:
    print("Greater than 3")
else:
    print("Less than 2 or between 2 and 3")

# while loops
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(x)

# interrupt the for loop to continue or exit the for loop under a certain condition.
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     #quit the loop
    print(x)

# The above loop prints 0,1,2,4

## Boolean

one_is_less_than_two = 1 < 2          # equals True
true_equals_false = True == False     # equals False

# Python uses the value None to indicate a nonexistent value. It is similar to other languages’ null:
x = None

# assert allows you to test if a condition in your code returns True.  If not, the program raises AssertionError
# You can wrtie a message to be written if code return False
assert x==None, "This is not the Pythonic way to check for None!"
assert x is None, "This is the Pythonic way to check for None!"

x = "hello"
#if condition returns True, then nothing happens:
assert x == "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye"

# Pretty much everything in Python is treated as True, except for:
    # False, None, [] (empty list), {} (an empty dict), "", set(), 0, 0.0
# Thus, I can use if statements to test for empty lists, empty strings, empty dictionaries, and so on.

# For example: safe_x = x if x is not None else 0
# The above set all x to 0, provided that it is not None.

## All, and any functions

# All: Takes an iterable (ex: list) and returns True when EVERY element is "Truthy" (not False, None, [], 0, etc...)
# Any: Takes an iterable (ex: list) and returns True when at least one element is "Truthy"

all([True, 1, [3]]) # True, since all elements of the list are truthy

all([True, 1, {}]) # False, since one of the element is an empty dict

any([True, 1, {}]) # True, since I have at least one truthy element

all([]) # True, since no falsy element in the empty list

all([[]]) # False, since the only element in the list is an empty list (falsy element)

## Sorting

x = [4,1,2,3]
y = sorted(x)
print(y)  # 【1，2，3，4】  default is smallest to largest

x.sort() # inplace sorting
print(x)


# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]
print(x)



# Suppose you have a document and you want to count the freq of each vocab
doc = ["henry", "is" , "a" , "data", "data", "scientist", "scientist", "scientist",
       "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]

from collections import defaultdict

word_counts = defaultdict(int) # int() produces 0
for word in doc:
    word_counts[word] +=1

print(word_counts)

# sort word_counts from highest to lowest count
wc = sorted(word_counts.items(),
            key = lambda word_and_count: word_and_count[1],  # use the 2nd element of word_counts.items() as the key (the value as key)
            reverse=True)
print(wc)

# NOTE:
# key= lambda x: x[1]

# If I rewrite using a named function:

# def element_1(x):
#    return x[1]