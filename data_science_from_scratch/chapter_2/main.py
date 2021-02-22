''' Chapter 2: Python Review'
- A tutorial on common tricks and tools I can use in Python
'''


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Henry')

    # printing loops
'''
Pycharm has a shortkey:  ALT-SHFIT-E that allows you to copy and paste selected lines to the Python Console

Use CTRL-R to run the entire project
Use CRTL-D to run the entire project in debug mode

Use CRTL-SHIFT-R to run ONLY main.py
Use CRTL-SHIFT-D to run ONLY main.py in debug mode

'''



'''
for i in [1,2,3,4,5]:
    print(i)

for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5]:
        print (j)
        print(i+j)
    print("done logging!")
'''
# ----------------------------------------------------------------

    # Use \ to continue line
    x = 1 + 2 + 3 + \
        4
    print(x)

# ------------------------------------------------------------

    # Import module that contain functions/constants for working with regular expressions
    import re as regex

    my_regex = regex.compile("[0-9]+", regex.I)

# ------------------------------------------------------------

    # If I only need a few specific functions from a module, use "from [module] import X, Y ...."
    from collections import defaultdict, Counter

    lookup = defaultdict(int)
    my_counter = Counter()


# ------------------------------------------------------------

    # Functions

    def double(x):
        return x * 2


    print(double(2))


    # ------------------------------------------------------------

    # Python functions are "first class", meaning I can:
    # Assign a function to a variable
    # Then pass the variable (that represents the function) as an
    # argument to another function!

    def apply_to_one(f):  # the argument f is itself a function!
        # calls the function f with 1 as its argument
        return f(1)


    # assign a function to a variable
    double_var = double
    x = apply_to_one(double_var)
    print(x)  # 2

    # ------------------------------------------------------------
    # Lambda to create short and anonymous functions
    # lambda [arg]: [content of function]

    y = apply_to_one(lambda x: x + 4)
    print(y)  # 5


    # ------------------------------------------------------------

    # Function parameters can be given default values
    def my_print(message="This is my default message!"):
        print(message)


    my_print("hello")  # hello
    my_print()  # default message


    # specify the names of the arguments.
    def full_name(first="What's-his-name", last="Something"):
        return first + " " + last


    print(full_name())
    print(full_name("Henry", "Fung"))

    # ------------------------------------------------------------

    # Strings

    # Python uses \ to indicate special characters

    tab_string = "\t"  # represents the tab character
    not_tab_sting = r"\t"  # represents '\t'
    print(tab_string + " " + not_tab_sting)

    # Using three double quotes, I can create multi-line strings
    multiline_string = """ This is the first line.
    And this is the second line.
    And this is the third line."""
    print(multiline_string)

    # ------------------------------------------------------------

    # f-strings provide a simple way to sub values into strings  (only available Python 3.6 or newer)

    first_name = "Joel "
    last_name = "Grus"

    full_name = f"{first_name}{last_name}"
    print(f"{first_name}{last_name}")

    # Alternatively
    print("{} {}".format(first_name, last_name))

    # ------------------------------------------------------------

    # Exceptions

    # When something is wrong, Python raises an exception.  If "unhandled", exceptions will cause
    # your program to crash. You can handle them using try and except.

    try:
        print(0 / 0)  # division by 0
    except ZeroDivisionError:  # use except to "catch or handle" the exception that would have cause program to crash
        # tell user no division by 0 without the program crashng.  This is only executed if an exception is thrown (error is encountered)
        print("Cannot divide by zero!")

    # ------------------------------------------------------------

    # Lists (Python has 0-based vectors)

    integers = [1, 2, 3]
    hetro_list = ["a", 1, True]
    list_of_lists = [integers, hetro_list]
    print(list_of_lists)

    list_length = len(integers)  # 3
    list_sum = sum(integers)  # 6

    print(list_sum)

    # ------------------------------------------------------------

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    zero = x[0]  # 0
    nine = x[-1]  # get first element from the right
    seven = x[-3]  # get third element from the right
    print(seven)

    # overwrite elements
    x[0] = 22  # first number is now 22

    # ------------------------------------------------------------

    # Slicing lists [a,b)

    print(x[:3])  # first 3 elements  index 0,1,2
    print(x[3:])  # index 3 to the end
    print(x[1:5])  # [1,2,3,4]  include index 1, exclude index 5
    print(x[-3:])  # [7,8,9]
    print(x[1:-1])  # without first and last elements
    copy_of_x = x[:]  # [22,1,2,...9]

    # ------------------------------------------------------------
    x = [22, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Every three elements
    print(x[::3])  # [22,3,6,9]
    print(x[1:6:2])  # [1,3,5]    [start:end:step]
    print(x[5:2:-1])  # start is index 5 (inclusive), end is index 2 (exclusive), step is -1 [5,4,3]

    # --------------------------------------------------------------

    # Use "in" to check if an integer is a member of a list
    # Check each element one at a time, so use this only if you know the list is small
    1 in [1, 2, 3]  # True
    1 not in [1,2,3] # False
    0 in [1, 2, 3]  # False

    # ----------------------------------------------------------------

    # Add elements to a list

    # Modify a list in place
    x = [1, 2, 3]
    x.extend([4, 5, 6])  # append 4,5,6 to the end of the list  (in place)
    print(x)  # [1,2,3,4,5,6]

    x + [4, 5, 6]  # not in place

    y = x + [4, 5, 6]  # y is [1,2,3,4,5,6,4,5,6], x is unchanged

    for i in (11, 22, 33):
        x.append(i)  # in place
    print(x)

    # ----------------------------------------------------------------

    # If I know how many elements there are in a list, I can unpack it
    x, y = [1, 2]  # x=1, y=2

    # If I don't care about 1, I can use a _ as a placeholder for the value you are going to throw away
    # I can print _ and will get 1.  So the use of _ as a placeholder is only an convention.

    _, y = [1, 2]

    print(y)

    # ----------------------------------------------------------------

    # Tuples

    # Tuples are immutable lists. EVERYTHING that you do to a list, you can do with tuples, EXCEPT you cannot modify them
    my_list = [1, 2]
    my_tuple = (1, 2)

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

    def sum_and_products(x, y):
        _sum = x + y
        _product = x * y
        return _sum, _product # this is a tuple


    print(sum_and_products(2, 3))  # (5,6)

    s, p = sum_and_products(5, 10)  # s is 15, p is 50

    # Both tuples and lists can be used for multiple assignments

    x, y = 1, 2
    x, y = y, x  # swap variables.  x gets y's value, y gets x's value

    # ----------------------------------------------------------------

    # Dictionaries

    # Dictionaries associate values with keys. I can retrieve a value in a dict with its corresponding key.
    # Dictionary keys must be “hashable”; in particular, you cannot use lists as keys.

    empty_dict = {}

    grades = {"Henry": 99,
              "John": 80}

    henry_grade = grades["Henry"]  # 99

    # I get a KeyError if I ask for a key that is not in the dict.
    try:
        jen_grade = grades["Jen"]
    except KeyError:
        print("No grade for this person")

    # To avoid this issue, I should check for the existance of a key in a dict.
    # Membership checks are fast even in large dicts
    henry_has_grade = "Henry" in grades  # True
    jen_has_grade = "Jen" in grades  # False

    99 in grades  # the "in" clause only checks for keys in dicts and not for values in dicts

    # Another example for this:
    x = [1, 2, 3]
    3 in x  # True

    x = {"henry": 1, "john": 2, "kate": 3}
    3 in x  # False
    "kate" in x  # True

    # get method for dictionaries
    # I can use dict.get() to retrieve a value from a dict based on key.
    # If the key does not exist, you will get a user-specified default value rather than a KeyError

    henry_grade = grades.get("Henry", 0)  # 0 is the default value if "henry" DNE in the dict
    john_grade = grades.get("John", 0)

    jen_grade = grades.get("Jen", 0)  # 0
    jen_grade = grades.get("Jen", -1)  # -1
    jen_grade = grades.get("Jen")  # None

    # I can assign value to a key
    grades["Henry"] = 100
    grades["John"] = 70
    print(grades)

    # I can add elements in a dict
    grades["Exor"] = 1000
    print(grades)

    # Just like lists and tuples, I can find length of dict using len()
    x = [1, 2, 3]
    print(len(x))

    x = (1, 2, 3)
    print(len(x))

    print(len(grades))

    # I can have a mix of datatypes within a dict
    tweet = {
        "user": "joelgrus",
        "text": "Data Science is Awesome",
        "retweet_count": 100,
        "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
    }

    print(tweet)

    # I can print out ALL the keys
    print(tweet.keys())
    # I can print out all the values
    print(tweet.values())

    # I can use .item() to get an iterable of (key,values) tuples
    tweet_items = tweet.items()
    print(tweet_items)

    for k, v in tweet.items():
        print(f"The key is {k}, and the value is {v} \n")

    # To check for membership of a key in a dict, use the following
    "tweet_length" in tweet  # False

    # And not:
    "tweet_length" in tweet.keys()

    # To check for a value in a dict (slow but the only way to check)
    1000 in grades.values()



    # Defaultdict --------------------------------------------------------------

    # Suppose you have a document and you want to count the freq of each vocab
    doc = ["henry", "is", "a", "data", "data", "scientist", "scientist", "scientist",
           "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]

    # One approach is to create a dict in which the keys are the vocab and the value are the count.
    # If the word DNE in the dict, I add it to the dict.  I increment the count of each word if it exists already
    # in the dict.

    word_counts = {}  # init the dict
    for word in doc:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print(word_counts)

    # I can implement the same thing by using try and exception.
    # If the word DNE in the dictionary, I handle the exception by
    # adding it to the dict.

    word_counts = {}  # init the dict
    for word in doc:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1

    print(word_counts)

    # The third approach uses .get()
    word_counts = {}  # init the dict
    for word in doc:
        # save the previous count (the count before my dict update, if word DNE, then default its value to 0).
        previous_count = word_counts.get(word, 0)
        # update dict
        word_counts[word] = previous_count + 1

    print(word_counts)

    # ***** NEW APPROACH: defaultdict ********
    # A defaultdict is like a regular dictionary, except that when you try
    #  to look up a key it doesn’t contain, it first adds a value for it using
    #  a "zero-argument function" you provided when you created the defaultdict.

    # Suppose you have a document and you want to count the freq of each vocab
    from collections import defaultdict

    word_counts = defaultdict(int)  # outputs 0 for any keys that doesn't belong in word_counts
    for word in doc:
        word_counts[word] += 1

    print(word_counts)

    # Defaultdicts are also useful with list of dict, or even your own functions

    dd_list = defaultdict(list)  # list produces an empty list
    dd_list["Lucy"].append(5)
    print(dd_list)  # The new key Lucy is associated with a list with element 5  {'Lucy': [5]}

    # a defaultdict of dicts
    dd_dict = defaultdict(dict)  # dict produces an empty dict
    dd_dict["Henry"]["my_key"] = "my_val"
    # The new key "Henry" is associated with a dict element, with "my_key" as its key and "my_val" as its value
    print(dd_dict)  # A dict of dicts

    dd_pair = defaultdict(lambda: [0, 0])  # define a function that outputs [0,0] for every new key
    dd_pair["John"][1] = 44  # change the second element to 44
    print(dd_pair)  # {'John': [0, 44]})

    # These defaultdicts will be useful when we’re using dictionaries to “collect”
    # results by some key and don’t want to have to check every time to see if the key exists yet.

    # Counters --------------------------------------------------------------------------

    # A counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts

    from collections import Counter

    c = Counter(["a", "a", "b", "c"])
    print(c)

    c = Counter([1, 1, 2, 3])
    print(c)  # Counter({0: 2, 1: 1, 2: 1})

    # I can use Counter to solve our word_counts problem
    doc = ["henry", "is", "a", "data", "data", "scientist", "scientist", "scientist",
           "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]
    word_counts = Counter(doc)
    print(word_counts)  # word_counts is a dict of each vocab in the doc (key) and the count of each word (val)

    # To get the most common three word, use the most_common() function of the Counter instance. Outputs a list of tuples.
    word_counts.most_common(3)

    for word, count in word_counts.most_common(3):
        print(word, count)




    # Sets -----------------------------------------------------------------------
    # Set is another useful data structure. It represents a collection of distinct items.

    # The difference between Tuples and Sets:
    # Both Tuples AND Sets are not mutable (you can't modified their elements)
    # You can everything else that lists can do
    # Tuples can have "repeated/non-unique" elements (7,7,8,4,4,1), but not set
    # Tuples are used in case we want to output 2 or more variables from a function.

    # Sets only contains unique elements
    # "in" clause works very fast on sets.
    # If we have a large collection of items that we want to use for a membership set, use set rather than list.
    # Use set to find a collection of distinct items in a collection.

    empty_set = set()  # don't use {}, that's an empty dict!

    primes_below_10 = {2, 3, 5, 7}
    4 in primes_below_10 # False


    s = set()  # init an empty set
    s.add(1)  # inplace add an element to the set  (for lists we use "extend", for sets we use "add")
    s.add(2)  # {1,2}
    s.add(2)  # still {1,2} since set only contains unique elements

    print(len(s))  # 2
    2 in s  # True
    3 in s  # False

    # Use set to check membership for a very large collection of things
    # stopwords_set = set(stopwords_list)
    # "has" in stopwords_set      # very fast to check

    # Use set to find distinct items in a collection
    item_list = [1, 2, 3, 1, 2, 3]
    num_items = len(item_list)  # 6
    item_set = set(item_list)  # convert list to set
    num_distinct_items = len(item_set)  # 3
    distinct_item_list = list(item_set)  # [1,2,3], convert back to list
    print(distinct_item_list)




    # Range -------------------------------------------------------
    # include start_value, exclude stop_value  [a,b)
    # range(start_value = 0, stop_value, step_size = 1)
    for i in range(5):  # if only 1 number, then we have only stop_value:  range(stop_value=5)
        print(i)  # 0 1 2 3 4

    for i in range(2, 6):
        print(i)  # 2 3 4 5

    for i in range(2, 6, 2):
        print(i)  # 2  4

    # Control flow ---------------------------------------------------

    # if....elif....else
    x = -1
    if x > 2:
        print("Greater than 2")
    elif x < 0 :
        print("less than 0")
    else:
        print("between 0 and 2")

    # while loops
    x = 0
    while x < 10:
        print(f"{x} is less than 10")
        x += 1

    # for loops
    # range(10) is the numbers 0, 1, ..., 9
    for x in range(10):
        print(x)

    # continue and break in for loops
    # interrupt the for loop under a certain condition to "continue" or under a certain condition to exit the loop.
    for x in range(10):
        if x == 3:
            continue  # go immediately to the next iteration and ignore all subsequent/remaining statements in the loop
        if x == 5:
            break  # quit the loop
        print(x)

    # The above loop prints 0,1,2,4



    # Boolean ----------------------------------------------------------------------------

    one_is_less_than_two = 1 < 2  # equals True
    true_equals_false = True == False  # equals False

    # Python uses the value None to indicate a nonexistent value. It is similar to other languages’ null:
    x = None

    # assert allows you to test if a condition in your code returns True.  If not, the program raises AssertionError
    # You can write a message to be presented  if code return False.  AssertionError: [message]
    assert x == None, "This is not the Pythonic way to check for None!"
    assert x is None, "This is the Pythonic way to check for None!"

    x = 1
    assert x == None, "This is not the Pythonic way to check for None!"
    assert x is None, "This is the Pythonic way to check for None!"

    x = "hello"
    # if condition returns True, then nothing happens:
    assert x == "hello"
    # if condition returns False, AssertionError is raised:
    assert x == "goodbye"

    try:
        assert x == "goodbye"
    except AssertionError:
        print("I have Assertion Error since x is not 'hello'!")

    # alternatively, I don't use try and except, instead:
    assert x == "goodbye", "I have assertion error since x is not 'hello'!"

    # Pretty much everything in Python is treated as True ("Truthy", except for:
    # False, None, [] (empty list), {} (an empty dict), "" (empty string), set() (empty set), 0, 0.0
    # Thus, I can use if statements to test for empty lists, empty strings, empty dictionaries, and so on.




    ## All and any functions -------------------------------------------------------------------------

    # All: Takes an iterable (ex: list) and returns True when EVERY element is "Truthy" (not False, None, [], 0, etc...)
    # Any: Takes an iterable (ex: list) and returns True when at least one element is "Truthy"

    all([True, 1, [3]])  # True, since all elements of the list are truthy (NOT 0, 0.0, None, [], set(), "", {}, False)

    all([True, 1, {}])  # False, since one of the element is an empty dict

    any([True, 1, {}])  # True, since I have at least one truthy element

    all([])  # True, since no falsy element in the empty list

    all([[]])  # False, since the only element in the list is an empty list (falsy element)



    # Sorting -------------------------------------------------------------------------
    # sorted(x, key=None, reverse=False)
    # key (Optional): A Function to execute to decide the order. Default is None
    # reverse=False is smallest to largest

    x = [4, 1, 2, 3]
    y = sorted(x)
    print(y)  # 【1，2，3，4】  default is smallest to largest

    x.sort()  # inplace sorting
    print(x)

    # sort the list by absolute value from largest to smallest
    x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]
    print(x)

    # Suppose you have a document and you want to count the freq of each vocab
    doc = ["henry", "is", "a", "data", "data", "scientist", "scientist", "scientist",
           "and", "he", "is", "waiting", "waiting", "for", "job", "job", "offer"]

    from collections import defaultdict

    word_counts = defaultdict(int)  # int() produces 0
    for word in doc:
        word_counts[word] += 1

    print(word_counts)

    # sort the dict "word_counts" from highest to lowest count
    wc = sorted(word_counts.items(),
                key=lambda x: x[1],  # input arg: content of function.  key= sort by output of a user-specified function.
                # use the 2nd element of word_counts.items() to decide the sorting
                reverse=True)
    print(wc)

    # NOTE:
    # key= lambda x: x[1]

    # If I rewrite using a named function:

    # def element_1(x):
    #    return x[1]


    # List Comprehensions ------------------------------------------------------------------------------------

    # Uses: transform a list into another list by choosing only certain elements, or by transforming elements.

    even_numbers = [x for x in range(5) if x % 2 == 0]  # [0,2,4]
    print(even_numbers)

    even_numbers2 =[]
    for x in range(5):
        if x%2==0:
            even_numbers2.append(x)
    print(even_numbers2)

    squares = [x * x for x in range(5)]  # [0, 1,4, 9, 16]
    print(squares)

    squares2 =[]
    for x in range(5):
        squares2.append(x*x)

    print(squares2)

    even_squares = [x * x for x in even_numbers]  # [0,2,4]
    print(even_squares)  #[0,4,16]


    # I can similarly use list comprehension to create dicts (or sets)
    square_dict = {x: x * x for x in range(3)}  # {0:0, 1:1, 2:4}
    print(square_dict)
    square_set = {x * x for x in [1, -1]}  # {1}, if not set then I would get [1,1]
    print(square_set)

    print([x*x for x in [1,-1]]) # [1,1]

    # If you don’t need the value from the list, it’s common to use an underscore as the variable:
    print(even_numbers)
    zeros = [0 for _ in even_numbers]  # [0,0,0], the resulting list have same the length as even_numbers
    print(zeros)

    # A list comprehension with multiple for loops
    pairs = [(x, y)
             for x in range(10)
             for y in range(10)]  # 100 pairs (0,0) (0,1) ... (9,8), (9,9)

    # only pairs with x < y  [(0,1),(0,2),...(0,9),(1,2),(1,3),...(1,9), (2,3), ... (8,9)]
    increasing_pairs = [(x, y)
                        for x in range(10)  # range(lo, hi) equals
                        for y in range(x + 1, 10)]  # [lo, lo + 1, ..., hi - 1]

    print(increasing_pairs)



    #  Automated Testing and Assert ------------------------------------------------------------------------

    # How can we be confident that our code is correct?  One way is to use types (discussed later),
    # Another way is to use automated tests (in this book we will only use assert statements).

    # Assert statements cause your code to raise an AssertionError if your condition is not truthy (not False, None, empty list, dicts, sets, tuples).
    # If it is Truthy, then nothing happens.
    assert 1 + 1 == 2 # 1+1==2 returns True, so nothing happens
    assert 1 + 1 == 2, "1+1 should equal 2 but didn't"  # optionally add a message to be printed if assertion fails


    # Usually, I use assert on functions you write to see if they are doing/outputting values that you expect:

    # This function returns the smallest value of a list
    def smallest_item(xs):
        return min(xs)

    # tests
    assert smallest_item([10, 20, 5, 40]) == 5

    assert smallest_item([1, 0, -1, 2]) == -1


    # You should use assert in this manner A LOT throughout your code!
    # If you look at the book’s code on GitHub, you will see that it contains
    # many, many more assert statements than are printed in the book.
    # This helps me be confident that the code I’ve written for you is correct.

    # More rarely, I use assert to check inputs to function

    def smallest_item(xs):
        assert xs, "I get empty list, we can't have min for an empty list!"
        return min(xs)

    smallest_item([])

    # Object-oriented programming -----------------------------------------------

    # I can define class that encapsulate data and the function that operate on them.
    # We use class occasionally to make code cleaner and simplier.
    # See more of this in Cory Schafter's notes.

    # I will create a "Clicker" class. This class maintains a count, which can be clicked to
    # increment a count.
    # You can also read count using a "read_count" function,
    # You can reset the count back to zero.

    '''A class can and should have a doc string, just like a function'''


    # A class can have zero or more member functions.  By convention, each function
    # takes a first parameter "self" that refers to the particular class instance.

    # A class also must have a constructor named __init__.  It takes whatever parameters you
    # need to construct an instance of your class.

    class CountingClicker:
        def __init__(self, count=0): # constructor
            self.count = count


    # instantiate the class
    clicker1 = CountingClicker()  # init to zero since default value that count (argument to the constructor) is zero.
    clicker2 = CountingClicker(10)  # clicker is init to 10


    # __XXX___ are known as "magic" methods (or dunder methods) in Python.
    # Class methods with names that start with an underscore are considered private (by convention).
    # User cannot by convention call private methods outside of the class itself (but Python does not stop users from doing so)

    class CountingClicker:
        def __init__(self, count=0):
            self.count = count

        # __repr__ produces the string representation of a class instance.
        def __repr__(self):
            return f"CountingClicker(count={self.count})"

        # The public API of our class
        def click(self, num_times=1):
            # increment the clicker some number of times, default is 1
            self.count += num_times

        # return the number of counts
        def read(self):
            return self.count

        # reset the clicker
        def reset(self):
            self.count = 0  # reset to 0


    # Now, we use assert to write some test cases for our clicker
    clicker = CountingClicker()  # instantiate clicker
    assert clicker.read() == 0, "clicker should start with count 0"

    # click twice
    clicker.click()
    clicker.click()

    assert clicker.read() == 2, "after two clicks, clicker should read 2."

    clicker.reset()
    assert clicker.read() == 0, "after reset, clicker should be back to 0."

    # Use repr: https://www.journaldev.com/22460/python-str-repr-functions

    clicker.click()
    clicker.click()
    print(clicker.__repr__())
    # or
    print(clicker)

    # Writing tests like these help us be confident that our code is working the way it’s designed to,
    # and that it remains doing so whenever we make changes to it.

    # Class inheritance

    # We’ll also occasionally create classes that inherit some of the functionality from a parent class.
    # For example, we could create a non-reset-able clicker by modifying the CountingClicker class.
    # We use CountingClicker as the base class and then modify the reset method so it does nothing.

    # This class has all the same methods as CountingClicker
    class NoResetClicker(CountingClicker):  # inherit from CountingClicker as base class
        # modify the reset method
        def reset(self):
            pass  # do nothing


    clicker2 = NoResetClicker()

    assert clicker2.read() == 0, "clicker should start at 0."
    clicker2.click()
    assert clicker2.read() == 1, "clicker should read 1 after one click."
    clicker2.reset()
    assert clicker2.read() == 1, "clicker should remain at 1 since reset does nothing."


    # Iterables and Generators ----------------------------------------------------------------------------

    # A list of a billion elements takes up a lot of memory.  If
    # I want to access elements one at a time, we shouldn't keep all
    # 1 billion elements in memory in a list.

    # We want instead generators that allow us to iterate over them like lists
    # but with values that are generated on demand.

    # One way is to create "generators" with functions that uses
    # the "yield" operator

    def generate_range(n):
        i=0
        while i<n:
            yield i # every call to yield
            # produces a value of the generator
            i+=1

    # The following loop will "consume" the yielded value one at a time
    # until none are left

    for i in (generate_range(10)):
        print(f"i is {i}")


    # I can even construct a generator that creates an infinite sequence
    def natural_numbers():
        '''returns 1,2,3,4.....'''
        n=1 # init the first value
        while True:
            yield n # generate n on demand everytime I call the function
            n+=1 # increment by 1

    for i in natural_numbers():
        if i > 20:
            break

        print(f"i is {i}")

# The flip side of laziness is that you can only iterate through a generator once. If you need to iterate
# through something multiple times, you’ll need to either re-create the
# generator each time or use a list. If generating the values is expensive,
# that might be a good reason to use a list instead.

# We can create generators from functions that uses "yield"
# Another way to create generators is to use list comprehensions wrapped in ()

even_num_lt_20= (i for i in range(20) if i%2==0)

# even_num_lt_20 is a generator that does not hold 0,2,4,...,18 (the entire
# sequence) in memory, but it will output each value of the sequence on demand as we
# iterate through even_num_lt_20

for i in even_num_lt_20:
    print(f"i is {i}")

# Such a “generator comprehension” doesn’t do any work until
# you iterate over it (using for or next).
# We can use this to build up elaborate data-processing pipelines:

# None of these computations *does* anything until we iterate
data=natural_numbers()
even_nums=(x for x in data if x%2==0)
even_squares=(x**2 for x in even_nums)
even_squares_end_in_six=(x for x in even_squares if x%10==6)

# generate one value at a time from even_squares by iterating over it
for i in (even_nums):
    if i>=30:
        break
    print(f"i is {i}") # 0, 2, 4, ...28


even_nums.__next__() # 32
even_nums.__next__() # 34
even_nums.__next__() # 36


# Enumerate ------------------------------------------------------------
# Often, when we iterate over a list or a generator, we want BOTH the values and their indices.
# To do this, we can use the "enumerate" function, which gives tuple (index, value)

names=["Henry", "Jennifer", "Bob", "Joe"]

for i, name in enumerate(names):
    print(f"The {i} th name is {name}")

# Randomness --------------------------------------------------------------

# In Data Science, we frequently need to generate random numbers.
# We can use the random module in Python.
# We will  most frequently use a function called "random" in this module

import random

random.seed(10) # this ensure we get the same result every time so our code is reproducible
# we are only interested in generating four random numbers drawn from unifrom distribution
# between 0 and 1
# (the resulting list should have the same length as range (4) )
four_unif_rand = [random.random() for _ in range(4)]

print(four_unif_rand)

# Using random.random(), I generate a number (a [0,1] number drawn from
# the uniform distribution based on seed
random.seed(10)
print(random.random())

random.seed(42)
print(random.random())

# Use the randrange(low,high) function to randomly choose two integers between
# [low,high)
random.randrange(10) # randomly choose a integer from [0,10)

random.randrange(3,6) # randomly choose a integer from [3,6)

# random.shuffle() randomly reorders the elements of a list
up_to_ten=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(up_to_ten) # randomly shuffle up_to_ten (with replace)
print(up_to_ten)

# If you need to randomly pick on element from a list, use random.choice()
my_friends = ["Alice", "Bob", "Charlie"]
my_best_friend = random.choice(my_friends)
print(my_best_friend)

# random.sample(): Randomly choose a sample of elements WITHOUT REPLACEMENT
my_numbers=range(0,60)
winning_numbers = random.sample(my_numbers, 5)
print(winning_numbers) #randomly sample 5 numbers from my_numbers without replacement

# To sample elements with replacement, make multiple calls of random.choice()
my_numbers=range(5)
rand_sample_with_replacement = [random.choice(my_numbers) for _ in range(10)]
print(rand_sample_with_replacement)


# Regular expressions ----------------------------------------------------------------------
# Used to search text, uses the module "re"

import re

re_examples=[not re.match("a","cat"), # cat doesn't start with a, therefore True
             re.search("a","cat"), # cat has an a in it, therefore True,
             not re.search ("c", "dog"), # dog doesn't have an c in it, therefore True
             3==len(re.split("[ab]","carbs")), # split string on a or by to ['c','r','s']
             "R-D-"==re.sub("[0-9]","-","R2D2") # replace any digits 0-9 in "R2D2" with dashes "-"
             ]
assert all(re_examples),"One element in list is False"

# re.match checks whether the beginning of a string matches a regular expression
not re.match("h","henry") # False
not re.match("f","henry") # True

# re.search checks whether ANY part of a string mathes a regular expression
not re.search("x", "henry") # True
not re.search("y", "henry") # False

# split a string into a list of strings, with the first argument as "separators"
re.split("[ab]","cchharbs12")  # ['cchh','r','s12']


# Functional Programming --------------------------------------------------------------------

# Author thinks that the Python functions:
    # partial
    # map
    # reduce
    # filter
# should be best avoided. Their use should be replaced be list comprehensions, for loops,
# and other more "Pythonic" constructs

# zip
# zip two or more iterables together.  The zip() function transforms multiple
# iterables into a single iterables of tuples

list1=["a","b","c"]
list2=[1,2,3]

zip(list1,list2) # an generator-like iterable

# Access each element of this iterable and put it in a list using list comprehension
combined = [p for p in zip(list1,list2)]
print(combined)

# NOTE: if the lists are different length, then zip stops as soon as the shorter list ends
list1=["a","b","c","d","e"]
list2=[1,2,3]

combined = [p for p in zip(list1,list2)]
print(combined) # [('a', 1), ('b', 2), ('c', 3)]

list1=["a","b","c"]
list2=[90,100,110,120,130]

combined = [p for p in zip(list1,list2)]
print(combined) #[('a', 90), ('b', 100), ('c', 110)]

# Unzipping a list of tuples into two tuples
pairs=[('a',1),('b',2),('c',3)]

letters,numbers=zip(*pairs)
print(letters) #('a','b','c')
print(numbers) # (1,2,3)

# The * performs "argument unpacking", which uses the elements of "pairs"
# as individual arguments to zip

# This is same as:
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

# In general, I can use * to perform argument unpacking for any function
def add(a,b):
    return a+b

add(1,2) # get 3  the add function takes two arguments

try:
    add([1,2]) # try putting the arguments in a list
except TypeError:
    print("add expects two inputs, rather than a list that contains two arguments")

# If I want to use a list of arguments for add(), use* to do "arguments unpacking"
# The elements in the list of arguments will be used as arguments to the function

add(*[1,2]) # get 3

my_arg=[1,2]
add(*my_arg) # get 3


# args and kwargs ------------------------------------------------------------------
# We want to create  function that:
    # takes another function f as the input argument
    # returns a new function that for any input, returns twice the value of f

def doubler(f):
    # Here, we define a new function that keeps a reference to f
    def g(x):
        return 2*f(x)
    # return that new function
    return g

# This works in *some* cases
def f1(x):
    return x+1

g=doubler(f1)

assert g(3)==8, "(3+1)*2 should equal to 8"
assert g(-1)==0, "(-1+1)*2 should equal to 0"

# This will not work with functions that takes for than one argument
def f2(x,y):
    return x+y

g=doubler(f2)

try:
    g(1,2)
except TypeError:
    print("As defined in doubler, g only takes on argument")

# Solution: we need to specify a function that takes
# arbitrary arguments, we do this with argument unpacking
# and a bit of magic

def magic(*args, **kwargs):
    print("unamed args:",args)
    print("keyword args:", kwargs)

magic(1,2, key="word", key2="word2")

#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

# When we define a function like this,
# args is a tuple of its unnamed arguments, and
# kwargs is a dict of its named arguments.

# It works the other way too, if you want to use a list (or a tuple)
# and dict to supply arguments to a function:

def other_way_magic(x,y,z):
    return x+y+z

x_y_list=[1,2]
z_dict={'z':3}

assert other_way_magic(*x_y_list,  # same as other_way_magic(1,2,...)
                       **z_dict) ==6, "1+2+3 should be 6"


# This is one trick that we use to produce higher-order functions whose inputs
# can accept arbitrary arguments

def doubler_correct(f):
    '''works no matter what kind of inputs f expects'''
    def g(*args,**kwargs):
        '''whaever arguments g is supplied, pass them through to f'''
        return 2*f(*args,**kwargs)
    return g


def f2(x,y):
    return x+y

g=doubler_correct(f2)

assert g(1,2)==6, "doubler should work now"

# Normally, if we know exactly what arguments to accept in a function,
# we should be explict about it.  We should only use
# *args and **kwargs if we don't know how many arguments there should be in our function.


# Type annotations -----------------------------------------------------------------------

# Python is a dynamically typed language, meaning that it doesn't care about
# the types of objects we use, as long as we use them in valid ways

# using "+" on different objects: numbers, lists, and strings

def add(a,b):
    return a+b

assert add(10,5)==15, \
    "+ is valid for numbers"

assert add([1,2],[3]) ==[1,2,3], \
    "+ is valid for lists"

assert add('hi',' there')=='hi there', \
    "+ is valid for strings"

# try add(10, "five")
try:
    add(10,"five")
except TypeError:
    print("cannot add an int to a string")

# In a statically typed language, our functions and objects would have specific types
def add(a: int, b: int) ->int:  # The a: int, b: int are called "type annotations"
    return a + b

add(10,5) # okay
add("hi"," there") # you want this to be NOT okay,
# but Python treat this as okay since it is a dynamic type language

# In general, type annotations (a: int, b: int) -> int DON'T do anything.
# Even if we use these type annotations, add("hi"," there") still works
# But despite of this, there are several reasons why we should use
# these type annotations in your Python code:
    # (1) An important form of documentations.

# def dot_products(x:Vector, y:Vector)-->float:
    #xxxxxx
    #return (xxxxx)

    # (2) There are external tools like mypy that will read your code
    # inspect the type annotations, and let you know about
    # type errors BEFORE you ever run your code.
    # For example, if you ran mypy over a file containing
    # add("hi"," there"), it would warn you:

# error: Argument 1 to "add" has incompatible type "str"; expected "int"

    # Like assert testing, this is a good way to find mistakes in your code before
    # you ever run it.


    # (3) Having to think about the types in your code forces you to design
    # cleaner functions and interfaces

# def ugly_function_v1(value,operation):
# ....

# def ugly_function_v2(value:int,
#                    operation: Union[str,int,float,bool])->int:
    #....

    # Here, we have a function whose argument "operation" is allowed to be string, or int,
    # or float, or a bool.  It is likely that this function is fragile and difficult to use.
    # But it becomes clearer when types are made specific in the second version of this function.

    # (4) Using types annotations allows your editor to help you with things like autocomplete and
    # to get angry at type errors.



# How to write type annotations --------------------------------------

# For build-in types like int and bool, you can just use the type itself as the annotation
# ex: x:int, y:bool

# What if you have a list?

def total(xs:list) ->float:
    return sum(xs)

# This works, but the type is not specific enough for xs
# We want xs to be a list of floats, instead of say a list of strings

# The type module provides a number of parameterized types that we can use to
# be more specific

# note the capital L
from typing import List

def total(xs:List[float])->float:
    return sum(xs)


# Up until now, we only specified annotations for function parameters and return types.
# For variables themselves, it's usually obvious what the type is:

# This is how to type-annotate variables when you define them, but this is
# unnecessary-- it's obvious that x is an int.

x:int = 5

# However, sometimes it's not obvious:
values=[] # what is the type?
best_so_far=None # what is the type?

# In such cases, we will supply inline type hints

from typing import Optional

values: List[int] = []

best_so_far: Optional[float]=None  #allowed to be either a float or None

# The typing module contains many other types, only a few of which we will ever use

from typing import List, Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str,int]={"data":1, "science":2}

# lists and generators are both "iterable"
lazy=True

if lazy:
    evens: Iterable[int]=(x for x in range(10) if x%2==0)
else:
    evens=[0,2,4,6,8]

# tuples specify a type for each element
triple_tuple: Tuple[int, float,int] = (10,2.3,5)

# Since Python has first-class functions (functions that themselves can be input args of other
# functions), we need a type to represent those as well.

from typing import Callable

# The type hint says that repeater is a function that takes two args:
    # a string and an int, and returns a string

def twice(repeater: Callable[[str,int],str],
          s:str) ->str:
    return repeater(s,2)

def comma_repeater(s:str, n:int)->str:
    n_copies=[s for _in range(n)]
    return ', '.join(n_copies)


# As type annotations are just Python objects, we can assign them to variables to
# make them easier to refer to

Number = int
num_list = List[Number]

def total(xs:num_list) ->Number:
    return sum(xs)


# Check out the mypy documentation about Python type annotations and type checking.
# The author uses mypy while he is writing the book, but it won't be used in the examples
# in the book.