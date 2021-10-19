""" We will practice working with APIs by building an application that consumes an existing Public API.
We will look at stack overflow-- if I type in Python in the search window of stack overflow, I get a set of Python
related questions. I can actually access this set of questions via the Stack overflow Public API

Go to api.stackexchange.com, and then click documentation. Scroll down to the "On-site methods" section, and I will see
all the possible API endpoints (e.g., answers, answers/{ids}, answers/{id}/accept, comments, badges

Scroll down and click on questions. There is an example of how to envoke getting the questions:
/2.3/questions?order=desc&sort=activity&site=stackoverflow

The stuff after the ? are order=desc & sort=activity ....  these are called query parameters. They can be used to modify
the results/query from the API.

I can take the address "/2.3/questions?order=desc&sort=activity&site=stackoverflow" and paste it after
api.stackexchange.com to see what the query looks like in a browser

"https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"

THis is a large chunk of data-- very messy to look at.


If I click "run" button on the questions page
https://api.stackexchange.com/docs/questions#order=desc&sort=activity&filter=default&site=stackoverflow&run=true
I get data displayed in JSON

I have a list of questions (a list called items). Each question has tags, owner, is_answered characteristics/elements,
which themselves are lists of other elements.

Copy and paste "http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow" in the
Postman app. In the output window, I get the JSON data

We will come back to Postman later, now let's try to work with the API in Python

Use Alt-Shift-E to run selected section of code in PyCharm


"""



import requests
import json

# I use the Python request package to retreive data (using get method). Note that I need to use http instead of https
# The get function will return a response
response = requests.get('http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(response) # get 200 which indicates okay

print(response.json()) # get all the json data, that's the same stuff we get in Postman or request via web browser

print(response.json()['items']) # get a list of questions (a list of dictionaries, each representing a question)

# iterate over the list of questions
for question in response.json()['items']:
    print(question['title']) # print title (the last element of each question dict) of each question
    print(question['link']) # print web link of question, I can ctrl-click to open
    print()

# Maybe I can build an application that looks for "good" stackoverflow questions to answer before everyone else does
for question in response.json()['items']:
    if(question['answer_count']==0): # only print questions with answer_count==0
        print(question['title']) # print title (the last element of each question dict) of each question
        print(question['link']) # print web link of question, I can ctrl-click to open
        print()
    else:
        print('skipped')
        print()

# In sum, that's how a consume an endpoint of an API
