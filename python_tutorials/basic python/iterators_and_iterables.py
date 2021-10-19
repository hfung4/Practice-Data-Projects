# https://www.youtube.com/watch?v=jTYiNjvnHZY

#################### Recap ##################################:
# What does it mean for an object (ex: list) to be iterable? This means this object can be looped over with the for loop.
# For specifically, this object have a __iter__() method that returns an iterator.

# An iterator itself (ex: num is a list, then  i_num = iter(num) is an iterator) also has:
    # __iter__() that returns the same object (self)
    # __next__() that fetches the next value ONE AT A TIME
    # An iterator knows its current state (knows where we left off)
    # An iterator returns the next valu one at a time with the __next__() method.
    # If there is no next value, __next__() returns a StopIteration exception.

# I can also add this functionality to our classes (ie: make our objects an iterator) by adding __iter__()
# and __next__() methods to our class.  Thus, the object will be an iterator that can be looped over.

# Generators (created from generator_fcns (yield), or generator comprehension) are also iterators.

##################################################################



#  Iterators and Iterables

# Confusion in these two terms: for example,  a list is a iterable, but not an iterator

# Iterable: "something that can be looped over"

# A list:
nums = [1,2,3]
#Let's loop over
for num in nums:
    print(num)

# I can also loop over dicts, sets, strings
# If an object is iterable, it needs to have a dunder method called __iter__ ()

# To check if an object has a __iter__() dunder method, do the following:

print(dir(nums))  # Yes, nums (a list) has a __iter__() method; thus it is an iterable that can be looped over


# What does it mean to loop for something?
# In the background, the for loop is calling the __iter__() method for our object (in this case, the list), and this
# method returns an "iterator".  We then loop over an iterator.

# A list is iterable, but it is NOT an iterator.
# If we run __iter__() on our list (__iter__() exist for list by definition), then it will return an iterator


# Next: what is an iterator?
#An iterator is an object with a "state", so that it remembers where it is during iteration.
# An iterator also "knows" how to get its next value.  An iterator has a dunder __next__() method to get its next value

# A list is not an iterator, thus it only has __iter(), but no __next__()

# next(nums)  # same as num.__next__().  Since nums is a list with no __next__(), we get error


# Let's get the iterator for the nums list
i_nums = nums.__iter__()
# ALternatively:
i_nums = iter(nums)

# We see that the iterator i_nums has BOTH  __iter__() and __next__()
print(dir(i_nums))

# Why the iterator i_nums() has a __iter__() method?
    # It has to have a __iter__() method because an iterator i_nums is ALSO iterable.
    # However, if I apply iter(i_nums)  I will get back the same object (it just return "self")


# Let's print out next(i_nums)

print(next(i_nums)) # 1
print(next(i_nums)) # If I run next again, since i_nums "knows" its state (where we left off), it should print out the next value 2
print(next(i_nums)) # 3
print(next(i_nums)) # The iterator run out of values. I get the StopIteration exception.  A for loop knows how to handle this error.

# For loop
# Step 1: Get the iterator of our iterable object (ex: get i_nums from nums)
# Step 2: Get the next value with __next__()
# Step 3: Get next value until I get StopIteration error.

# What a for loop is really doing

moreNums = [1,2,3,4,5]

i_moreNums = iter(moreNums)
while True:
    try:
        item = next(i_moreNums) # get next value
        print(item)
    except StopIteration: # specify that I break out of loop if I get StopIteration exception
        break


## Practical example of iterators

# KEY: We can create our own objects (through Class)
# These objects ARE NOT iterators, unless we define our own __iter__() and __next__() method for them.
# Recall that if we call .__iter__() on an iterator, it will just return self (the same object)
# The __next__() method returns the next value

# Let's create a class that is same as the built-in range function

class MyRange:

    def __init__(self, start, end):
      self.value = start
      self.end = end

    def __iter__(self):  # We need to have a __iter__method for a MyRange object to be iterable
        return self      # Recall that if I call __iter__() on a iterator, it will return the same object (self)

    # The __next__() of an iterator returns the current value, and updates the next value
    # The __next__() method of an iterator has the following logic:
        # Save my current state
        # Update the current to the next value
        # return the (saved) current value
        # If the iterator runs out of values, return the stopIteration excception

    # We will replicate this logic in the method below:
    def __next__(self):
        # Check if there are any more values in the iterator (value>end).  If yes, raise exception
        if self.value >= self.end:
            raise StopIteration
        current = self.value  # save (keep track) the current state
        self.value += 1  # update self.value (get the next value)
        return current # return the current value


test = MyRange(1,10)  # create a MyRange object called "test", this object is an iterator since there is __iter__ and __next__

# KEY: I can use for loop to loop through the iterator "test"
# The for loop will automatically call iter(test)  (which returns the exact same object)
# Then it will perform next(test) until StopIteration occurs

for i in test:
    print(i)


# I can also call __next__() to get values one at a time

test2 = MyRange(1,10)

print(next(test2))
print(next(test2))
print(next(test2))



## Generators

# Generators can be created in two ways:
    # Generator comprehensions
    # A function with "yield"

# Generators are iterators, with __iter__() and __next__() created automatically


# Example: generator function

def my_range_gen_fcn(start,end):
    current = start
    while current < end:  # This loop will yield value from 1....9
        yield current  # output the current value
        current +=1 # update the current value


my_gen = my_range_gen_fcn(1,10) # my_gen is a generator, which is an iterator

# I can loop through a generator
for i in my_gen:
    print(i)


# __next__() is created automatically in generators, so I can get next value with __next__()

my_gen2 = my_range_gen_fcn(1,10)

next(my_gen2)
next(my_gen2)
next(my_gen2)


## As long as there is a "next" value, our iterator will continue to get the next value one at a time

def my_range_inf(start): # Always will have a next value
    current = start
    while True:
        yield current
        current +=1


my_gen3 = my_range_inf(1)

# I can get the next value indefinitely, BUT I still fetch the next value one at a time
# So I will not have any memory issue.  For example, imagine in case of having next value indefinitely,
# I have 100 billion values.
# I can get the values one at a time rather than (like a list) needing to store all 100 billion in my CPU memory
# and then do iteration.
# This is a MAIN ADVANTAGE of iterators (generators)-- I won't run out of memory
next(my_gen)
next(my_gen)
next(my_gen)
next(my_gen)
