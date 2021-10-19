# https://www.youtube.com/watch?v=bD05uGo_sVI&t=1s

# Generators:  Why do I want to use them?  And what are their advantages over lists




# This function take a list called "nums" and return a list with squared values
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_results = square_numbers([1,2,3,4,5])

#Alternatively

my_results = [x*x for x in [1,2,3,4,5]]

print(my_results)



## Alternatively I can output a Generator instead of a list

def square_numbers(nums):
    for i in nums:
        yield(i*i)


#my_gen is a generator (an iterator) instead of a list
my_gen = square_numbers([1,2,3,4,5])

# my_gen does not whole the entire results (the 5 squared numbers) in memory, instead it yields one sq number at a time

# my_gen actually has not computed ANYTHING yet.  It is waitng for us to ask for the next value

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))  # last value
print(next(my_gen))  # StopIteration Exception

# Use comprehension to create generator
my_gen = (i*i for i in [1,2,3,4,5])

# I can loop through the my_gen generator (an iterator, with __iter__() and  __next__() created automatically)
for i in my_gen:
    print(i)

# I can also convert (cast) a generator to a list (so all numbers will be in memory)
my_gen = (i*i for i in [1,2,3,4,5])
print(list(my_gen))




############ Performance Difference between a list and generator ####################

import random
import time

# A list of names
names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors= ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# size of list is specified by num_people
def people_list(num_people):
    result = []
    for i in range(num_people):
        #create a dictionary of id, names, and major.  I pick a name and a major randomly from the above lists
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        result.append(person)  # Append the dict to the result list, so I have a list of dicts

        return result # return the list of dicts


def people_gen(num_people):
    for i in range(num_people):
        #create a dictionary of id, names, and major
        person = {
            'id':i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


# Let's time the run-time of the people_list functions
t1= time.clock()
people = people_list(100000000)
t2=time.clock()

print('Took {} Seconds'.format(t2-t1))

# Let's time the run-time of the people_list functions
t1= time.clock()
people_gen = people_gen(100000000)
t2=time.clock()

print('Took {} Seconds'.format(t2-t1))

