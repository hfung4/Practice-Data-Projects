# https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=21&t=4s

# Easier and more readable way to write/read a list

##
# I want 'n' for each 'n' in nums
nums =[1,2,3,4,5,6,7,8,9,10]

# Using for loop
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# Using list comprehension  "I want 'n' for each 'n' in nums"
my_list = [n for n in nums]
print(my_list)


## I want 'n*n" for each 'n' in nums

my_list=[]

# Using for loop
for n in nums:
    my_list.append(n*n)
print(my_list)

#Using list comprehension
my_list=[n*n for n in nums]
print(my_list)


## Using map and lambda (not as common now, since we have list comprehension

# lambda allow us to define a function in the following form
#
# fcn_name = lambda input_arg: statements
#


sq_fcn = lambda n: n*n
sq_fcn(2) # 4


# Using map, I can run everything in the list through a function)
    # map(function, list)

nums=[1,2,3,4,5,6,7,8,9,10]

# define a function
def sq_function(n):
    return n*n

my_list=map(sq_function,nums)  # In Python 3, 'my_list' is an iterator (map object)


for r in my_list:
    print(r)


# I can define function using the 'compact way'-- lambda
my_list = map(lambda n: n*n, nums)   # In Python 3, 'my_list' is an iterator

for r in my_list:
    print(r)

## I want 'n' for each 'n' in nums if 'n' is even

nums=[1,2,3,4,5,6,7,8,9,10]
my_list=[]

# Using for loop
for n in nums:
    if n%2==0: # even number
        my_list.append(n)

print(my_list)


# Using list comprehension
my_list=[n for n in nums if n%2==0]
print(my_list)


## I can implement the above using the filter and lambda approach  (not readable)
my_list =[]

# Filter:  Runs a list through a function that performs filtering
    # filter(my filtering condition, list)

#use filter if I want to return an object in a list based on a condition defined in the fcn.
my_list=filter(lambda n: n%2==0, nums)
for r in my_list:
    print(r)


## I want a (letter, number) pair, for each lettter in 'abcd', and each number in '0123'
# expected output:
    # my_list =[(a,0),(a,1),(a,2),..., (d,3)]


# Using for loop
my_list=[]
my_str="abcd"  # a list of chars

for letter in my_str:
    for number in range(4): # [0,4)
        my_list.append((letter,number))  # append a tuple of (letter,num) to my_list at each iter

print(my_list)

# Using list comprehension
my_list=[]

# outer loop goes first, then inner loop
my_list=[(letter, number) for letter in my_str for number in range(4)]
print(my_list)

## Dictionary comprehensions

# It's not only lists we can do comprehension, we can also apply this to dicts and sets
names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip creates a list of tuples.  It takes the first element of names and the first element of heros and form a tuple,
# then the tuple is place in the list.  Then zip takes the second element of names, and seocond element of heros and
# forms a second tuple, then it appends it to the list, and so on
results=zip(names, heros)

for n, h in results:  # each element is a 2-tuple
    print("{}, {}".format(n, h))



names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# To make a dict
my_dict={} # empty dict
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)


# Do the above using dictionary comprehension

names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict ={name: hero  for name, hero in zip(names, heros)}
print(my_dict)

# NOTE: I can define a dict as follows
dict = {'a':1, 'b':2, 'c':3}
print(dict)

# NOTE 2: It is easy to add "restrictions at the end of these dict comprehensions.  For example
# what if I don't want Bruce to be on this dictionary?

names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict ={name:hero  for name, hero in zip(names, heros) if name!='Bruce'}
print(my_dict)


## Set comprehensions

# Tuple vs List:  Tuple is NOT mutable (can't be changed), while lists can be changed. I can only reassign all elements
# or delete all elements, or slice a tuple, but I can't change only a few elements, or remove only a few elements in a tuple

# Set is exactly like a list, but it has no repeating values.  Set is a collection of unique items
my_set={1,2,1,4,5,6,6}
print(my_set) # duplicated elements are excluded

# pop() function
# I can 'pop' a list, set, or dict  (pop.() will return the first element in a list/set/dict.  This
# element is popped, meaning that it is deleted from the original list/set/dict

my_set.pop() # return 1
print(my_set) # 1 is gone
my_set.pop()  # return 2
print(my_set) # 2 is gone

# Set comprehension

nums =[1,1,2,1,3,4,3,4,5,5,6,7,8,9,9]
my_set = set() # init an empty set

# Using for loop
for n in nums:
    my_set.add(n) # use .add() instead of .append() for sets
print(my_set) # sets only contain unique values

# Using set comprehension
my_set={n for n in nums}
print(my_set)

my_set={n for n in nums if n is not 9}
print(my_set)

my_set={n for n in nums if n !=9 }
print(my_set)


## Generators comprehension ((more about this in the generator module)

nums=[1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen= gen_func(nums) # Get a genrator object (an iterator)  gen is like a list, but all elements are not in memory
for i in my_gen:
    print (i)

# Alternatively
for i in gen_func(nums):
    print (i)


# Using comprehension
my_gen=(n for n in nums)
print(my_gen) # a generator object

for i in my_gen:
    print (i)