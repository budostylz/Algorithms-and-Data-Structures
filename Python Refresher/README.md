# Introduction to Python
https://www.udacity.com/course/introduction-to-python--ud1110

## Code and Syntax Highlighting
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code

## Bitwise Operators
https://wiki.python.org/moin/BitwiseOperators

## Python Operators
https://www.programiz.com/python-programming/operators

##  Floating Point Arithmetic: Issues and Limitations
https://docs.python.org/3/tutorial/floatingpoint.html

## PEP 8 -- Style Guide for Python Code
https://www.python.org/dev/peps/pep-0008/

## Why is 80 characters the 'standard' limit for code width?
https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width

## Learn Python Programming
https://www.programiz.com/python-programming

```python

# Examples of iteration with for loops
my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of item is: ' + str(item))

print('-----------------------------------------')

# Print each index and value pair.
for i, value in enumerate(my_list):
    print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))

    print('-------------------------------------')

# Print each number from 0 to 9 using a while loop.
i = 0
while(i < 10):
    print(i)
    i += 1



print('-------------------------------------')
# Print each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])

print('-------------------------------------')

my_dict2 = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict2:
    output.append(my_dict2[key][i])
    #print(my_dict2[key][i], my_dict2[key])
    i += 1
print(output)


# Control Statements
num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number equals 5.')
else:
    print('The number is greater than 5.')

#Practice
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    #print('in_list', in_list)
    smallest_pos = None
    
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos
        


# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2


# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    # TODO: Fill out the function here.
    #print(course, courses)

    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)

    
    # TODO: Return list of semesters here.
    return semesters



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b

print(sum(1,1))

# Example function 2: return the size of list, and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list

print(list_sort([3, 2, 1]))

# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print('doing something else...')

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))





```