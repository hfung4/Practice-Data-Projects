'''
https://www.youtube.com/watch?v=K8L6KVGG-7o&t=0s
https://www.youtube.com/watch?v=sa-TUpSx1JA&list=PL7IB9PHqa60PvnfrllPpmJyNBlgv4IIOW&index=13&t=1s

- Regular expression: main purpose is that it allow us to search for and match specific patterns of
text.
- In Python, there is a built-in re module for regular expression.
- A raw string in Python is a string that is prefix with a r.  r"abcc". This will tell Python not to
treat \ in any special way. Normally,\t is a tab. But with a r'\t aaa', Python will treat \ literally
- re.compile() is an important function that allow us to define and "save" our text pattern (
case-sensitive) in a variable
- finditer is another important function that gathers the index of all "matched patterns" in a list


'''

import re

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Use Alt-Shift-E to run selected code

def match_pattern_in_str(p:str, target_str:str):
    """Reads user specified string pattern and a target string, returns indices of matches in the
    target string

       Args:
           p (str): user defined text pattern (must be a raw string e.g., r"abc"
           target_str (str): target string to search in

       Returns:
           None
       """
    pattern = re.compile(p)
    matches = pattern.finditer(target_str)
    for match in matches:
        print(match)



text_to_search = ''' abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# First example -----------------------------------------------------------------------------------
# define my text pattern
pattern = re.compile(r'abc') # I want to search for pattern 'abc'

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) # returns indices of the matched pattern in my string

print(text_to_search[1:4]) # I can use the returned index from finditer to slice my text


# MetaCharacters that need to be escaped ----------------------------------------------------------
# . ^ $ * + ? { } [ ] \ | ( )
# These characters have special meaning in regex. So if we want to search literally "." in my text,
# I need to "escape it" by a backslash
# One application is if I have websites in my target strings e.g., google.com, I can search for "." by
# escaping the \.
match_pattern_in_str(r'\.',text_to_search)

match_pattern_in_str(r'coreyms\.com',text_to_search)


# How to use metacharacters in regex ---------------------------------------------------------------

#. Any number except for the newline
# pattern = re.compile(r'.')
match_pattern_in_str(r'.',text_to_search) # match all chars but new line

# \d matches any digit (0-9)
# pattern = re.compile(r'\d')
match_pattern_in_str(r'\d',text_to_search) # all matches are digits from 0-9

# \D matches anything that is NOT a digit
# In general, capitol means "NOT" (negate the lowcase version)
# pattern = re.compile(r'\D')
match_pattern_in_str(r'\D',text_to_search) # all matches are NOT digits from 0-9

# \w matches anything that is a word character (a-z,A-Z,0-9,_)
# pattern = re.compile(r'\w')
match_pattern_in_str(r'\w',text_to_search) # all matches are word chars

# \W matches anything that is NOT a word character anything other than (a-z,A-Z,0-9,_)
# pattern = re.compile(r'\W')
match_pattern_in_str(r'\W',text_to_search) # all matches are NOT word chars

# \s matches anything that is whitespace, which includes space, tab, newline
# pattern = re.compile(r'\s')
match_pattern_in_str(r'\s',text_to_search) # all matches are whitespace

# \S matches anything that is NOT whitespace
# pattern = re.compile(r'\S')
match_pattern_in_str(r'\S',text_to_search) # all matches are NOT whitespace

# Anchors -------------------------------------------------------
# These meta characters do not actually match a char, but rather it specifies positions BEFORE or
# AFTER chars.
# We use Anchors in conjunction with other patterns for searching

#\b: word boundaries, which is whitespace or anything that is NOT alphanumeric
# Example: Ha HaHa
# pattern = re.compile(r'\bHa')
match_pattern_in_str(r'\bHa',text_to_search)
# return two Ha
# It matches the first Ha, because the start of a line is a word boundary
# It matches the second Ha, because a whitespace is a word boundary
# It does not match the last Na because it is has a char before it and nothing after it

#\B: NOT word boundaries
# Example: Ha HaHa
# pattern = re.compile(r'\BHa')
match_pattern_in_str(r'\BHa',text_to_search)
# matches only the last Ha

# ^ Will match a position at the start of a string
# $ Will match a position at the end of a string

#sentence = 'Start a sentence and then bring it to an end'

match_pattern_in_str(r'^Start',sentence) # matches "Start" at the beginning of the string

match_pattern_in_str(r'^a',sentence) # since 'a' is not at the start of the string, even though
# it is in sentence, I get no match

match_pattern_in_str(r'end$',sentence) # matches 'end' at the end of the string
match_pattern_in_str(r'then$',sentence) # 'then' is in the sentence but since it is not at the end of
# the string, I get no matches


 # Practical examples -------------------------------------------------------------------

# Match these phone numbers within our multi-line string text_to_search
# 321-555-4321
# 123.555.1234

# The pattern that we have is: 3 digits, followed by a dash or period, 3 digits, followed by a dash or
# period, 4 digits.
# Let's create the pattern
p = r"\d\d\d.\d\d\d.\d\d\d\d"
match_pattern_in_str(p,text_to_search)

p = r"\d\d\d.\d\d\d.\d\d\d\d"
match_pattern_in_str(p,text_to_search)

# Let's try to find all the phone numbers in "data.txt"
p = r"\d\d\d.\d\d\d.\d\d\d\d" # my pattern

with open('data.txt','r') as f:
    contents = f.read()
    match_pattern_in_str(p,contents)

# What if I want to look for phone number that has - or .
# I need to do something called a "character set". Basically, I can use a [] to create a set of chars
# that I want to match
p = r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d' # notice I don't need to \. in char sets
match_pattern_in_str(p,text_to_search)

# Even though you have multiple char in a char set, Python only looks for . or - in A SINGLE character
# (the one that comes after \d and the one that comes before another \d
p = r'\d\d\d[.-A-Za-z0-9]\d\d\d[.-]\d\d\d\d' # here, I am trying to match . or - or upper case char or
# lower case char or digit for the char that comes after the \d and before another \d
match_pattern_in_str(p,text_to_search)

# Let's trying to match phone numbers starting with 800 or 900
p=r'[89]00[-.]\d\d\d[.-]\d\d\d\d' # we can use a char set for 8 or 9, followed by 00 (literal match)
match_pattern_in_str(p,text_to_search)

# - is a special char within a char set, but ONLY if it is placed between digits or letters. Otherwise,
# it is treated as a literal -
# If - is placed between digits r'[1-5]', we specify a range of values (including 1 and 5)
# # If - is placed between letters  r'[g-m]', we specify a range of letters (including g and m)

p=r'[1-5b-g]' # match any text 1-5 or b-g (we can put as many ranges back-to-back as we want in a char
# set)
match_pattern_in_str(p,text_to_search)

# ^ is another special char within a char set. If I put ^ at the start of the char set, it negates
# the char set, meaning Python will match anything that is NOT in the char set
p=r'[^1-5b-g]' # matches all chars that is NOT 1-5 or b-g
match_pattern_in_str(p,text_to_search)

p=r'[^a-zA-Z]' # matches all chars that is NOT uppercase or lowercase letters
match_pattern_in_str(p,text_to_search)

# I want to match all three letter words that end with a "t", EXCEPT for "bat"

three_letter_words = '''cat
mat
pat
bat
'''

p=r'[^b]at' # anything that is NOT b, followed by a literal 'at'
match_pattern_in_str(p,three_letter_words)



p = r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d'
match_pattern_in_str(p,text_to_search)

# I can easily make mistakes if I type out a lot of \d\d\d\d
# I can use something called a "quantifier" to match multiple chars at a time

# * matches 0 or more of the pattern that we are looking for (so the pattern is like an "optional thing")
# + matches 1 or more of the pattern that we are looking for
# ? matches 0 or one of the pattern that we are looking for
# {3} matches exactly 3 of the pattern that we are looking for
# {3,4} matches 3 to 4 of the pattern that we are looking for

# Instead of writing d\d\d\  I can write \d{3} so that Python will match 3 \d
p = r'\d{3}[.-]\d{3}[.-]\d{4}'
match_pattern_in_str(p,text_to_search)

# If we don't know (or don't want to specify) the exact number of pattern (say \d) that we are looking
# for, we need to use other quantifiers
'''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
# We have these names, some start with Mr. others with Ms or Mrs.
# Say I want to specify a pattern that matches these prefixes and the name that came afterwards
p=r'Mr\.' # matches all Mr.
p=r'Mr\.?' # matches Mr with . being 0 or 1 (optional)
match_pattern_in_str(p,text_to_search)

p=r'Mr\.?\s[A-Z][a-z]*' # Mr. followed by space, follwed by uppercase letter (I can use char set here),
# followed by smaller case letter (0 or more since I have Mr.T)
match_pattern_in_str(p,text_to_search)

# Alternatively
p=r'Mr\.?\s[A-Z]\w*' # Mr. followed by space, follwed by uppercase letter (I can use char set here),
# followed by a word char (0 or more since I have Mr.T)
match_pattern_in_str(p,text_to_search)

# Groups -------------------------------------------------------
# Let's try to match Ms and Mrs. names AND Mr Mr. names
# The best way to do this to use groups
# Groups () allow us to specify two or more patterns that we are looking for
# Within () I can use | which is the "OR" operator
p=r'M(r|s|rs)\.?\s[A-Z]\w*' # I have three different patterns to look for at the start of the string: Mr
# Ms or Mrs
match_pattern_in_str(p,text_to_search)

# Difference between char set [] and group
# char sets: matches a single character with the content inside the char set [as.-]
# group: matches a group of chars with with patterns inside the group (r|s|rs|abc|acd1)

# Alternatively (easier to read-- we can see exactly what group of chars that we are trying to match
# at the start of the string)
p=r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*' # I have three different patterns to look for at the start of the
# string: MrMs or Mrs
match_pattern_in_str(p,text_to_search)

# Recap examples --------------------------------------------------------------------------

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# match CoreyMSchafer@gmail.com
# Everything before the @ symbol is just uppercase or lowercase letters (one or more)
# literal @
# lower or upper case letters (one or more)
# literal .com
p=r'[a-zA-z]+@[a-zA-z]+\.com'
match_pattern_in_str(p,emails)


# To match CoreyMSchafer@gmail.com AND corey.schafer@university.edu
# Everything before the @ symbol is just uppercase or lowercase letters or . (one or more)
# literal @
# lower or upper cases letter (one or more)
#.edu or .com
# Again, I don't need \. inside group ()
p=r'[a-zA-z.]+@[a-zA-z]+(.com|.edu)'
match_pattern_in_str(p,emails)

# To match all three emails
# Everything before the @ symbol is just uppercase or lowercase letters or . or - or digits (one or more)
# literal @
# lower or upper cases letter or - (one or more)
#.edu or .com or .net
p=r'[a-zA-z0-9.-]+@[a-zA-z-]+(.com|.edu|.net)'
match_pattern_in_str(p,emails)

# As you can see, it's pretty hard to write patterns that matches email address
# On the Internet, there are lots of "pre-written" email patterns already.
# If you know regex, then you can also read other people's regex (though it is much harder in general
# to read regex as opposed to building your own regex)

# Can you read what this regex is doing? -------------------------------------------------
# r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Matches more than one of the following: all lowercase and uppercase letters, all digits, underscore,
# + or .
# literal @
# Matches one or more of the following: all lowercase and uppercase letters, all digits, -
# literal .
# Matches one or more of the following: all lowercase and uppercase letters, all digits, - or .


# How to capture information from groups -------------------------------------------------
# We have already seen how to match patterns of groups
# We can actually also use the information we captured from groups

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# Some are http, others are https
# Some have www. others do not

# Let's say I want to "grab" google.com, coreyms.com, youtube.com, and nasa.gov

# But first, let's try to match ALL the urls
# literal http
# Zero or more s
# literal ://
# Zero or more www
# One or more word char
# literal .
# One or more word char
pattern = re.compile(r'https?://(www.)?\w+\.\w+')
matches = pattern.finditer(urls)

for match in matches:
    print(match)

# Use groups to capture some info from the urls
# Let's try to capture the domain name (youtube or nasa) and the top-level domain (.gov, .com)

# In my pattern, I put () around the domain name and top-level domain and make them into a group
# pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

# This shouldn't change my results
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match)

# But now, I have three different groups in my pattern
# 1. the optional www.   (www.)?
# 2. domain name   (\w+)
# 3. high-level domain   (\.\w+)
# 4. I also have a "group zero", which is the entire url that I captured, for example
    # (https://www.google.com)

# The match object that we are iterating through actually has a "group method". I can pass the index
# of the group that I want to see to this method

pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0)) # group zero is the entire url (pattern)


# group 1 (optional www.)
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(1)) # optional www., I will print None for urls that do not have www.


# group 2 (domain name)
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2)) # domain names


# group 3 (high-level domain)
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(3)) # high-level domain


# Back-referencing of groups -----------------------------------------------------

# Let's look at example first, and then we will explain what this does

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

# pattern (or the output object of re.compile) has a method called sub()
# The sub() allow us to perform replacement in a string (in our case, urls)
# The first argument is the replacement, and the second argument is the string that we want to do
# replacement on.
# We can use \1 \2 \3 to refer to group 1, group 2, group 3 that I specified in "pattern"

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# To recap:
    # We created a pattern that matches all urls in our multi-line url string
    # We specify 3 +1 groups in our pattern
    # We substitute (replace) the matches with group 2 and 3 \2\3. Every time Python finds a match,
# it will sub that match with group 2 (domain name) and group 3 (high level domain)
    # subbed_urls is a new string that contains all the substitutions that was made

# Use-case: if I have a large document and I want to replace certain text, this is a very efficient
# way to do it


# Other re methods -----------------------------------------------------------------------------
# This method does the best job in showing matches and all the location of the matches (in indices)
# There are other that we can use for other purposes

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# findall just return matches as a list of strings (so no information like indices). But it will only
# match the first group that you specify (Mr, Ms Mrs)
# If there are multiple groups, then matches would be a list of tuples [(group 1, group 2),...]
matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

''' Output
Mr
Mr
Ms
Mrs
Mr
'''

# findall: return matches as a list of strings (so no information like indices).
# If pattern contains no groups, it will return all matches in a list of strings
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

''' Output
321-555-4321
123.555.1234
800-555-1234
900-555-1234
'''

# Match function: find out if there is a match of my pattern at the BEGINNING of the string
# if yes, it will return text and indices; Otherwise, it will return none

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'Start')
# Even though there are two "Start" in sentence, .match() only returns the first match
match_at_beginning = pattern.match(sentence) # returns the first match of the pattern

print(match_at_beginning)

'''Output
<re.Match object; span=(0, 5), match='Start'>'''

# If 'Start' is not at the beginning of the string, match will return none
sentence = 'A sentence is Start and then bring it to an end'

pattern = re.compile(r'Start')
# Even though there are two "Start" in sentence, .match() only returns the first match
match_at_beginning = pattern.match(sentence) # returns the first match of the pattern

print(match_at_beginning)

'''Output
None
'''


# search function: find out if there is a match of my pattern at any part of my string
# If there are two 'Start' in my string, the match functionONLY returns the first 'Start'
# Return none if the pattern does not exist in the string

sentence = 'Start A sentence is Start and then bring it to an end'

pattern = re.compile(r'Start')
# Even though there are two "Start" in sentence, .match() only returns the first match
match_anywhere = pattern.search(sentence) # returns the first match of the pattern

print(match_anywhere)

'''Output
<re.Match object; span=(0, 5), match='Start'>
'''

# Flags (additional arguments for search or finditer etc... functions) ---------------------
# Let's say I want to match a word-- each char of the word can be uppercase, lowercase, or both

sentence = 'StaRT A sentence is Start and then bring it to an end'

# Normally, I need to create a char set of an uppercase S and lowercase of s, followed by
# another char set of T and t, and so on
pattern = re.compile(r'^[Ss][Tt][Aa][Rr][Tt]')

matches = pattern.finditer(sentence) # returns the first match of the pattern

for match in matches:
    print(match)

'''Output
<re.Match object; span=(0, 5), match='StaRT'>
'''

# Since this is such a pain, instead we can search for the literal text 'start', and then add a flag
# to our pattern
pattern = re.compile(r'start', re.IGNORECASE) # can also use re.I (short-form of the flag)
matches = pattern.finditer(sentence) # returns the first match of the pattern

for match in matches:
    print(match)

'''Output
<re.Match object; span=(0, 5), match='StaRT'>
<re.Match object; span=(20, 25), match='Start'>
'''

# There are other useful flags:
# For multiline string, there is a flag that allows us to use ^ and $ to look for matches at the start
# and end of a line (rather than of the entire string)
