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

def prod(a,b):
    # TODO change output to the product of a and b
    return a*b

def fact_gen():
    i = 1
    n = i
    while True:
        
        output = prod(n, i)

        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

# Examples of Python Classes
class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name

bob = Person('Bob', 32)
print(bob.getName())

bob.birthday()
print(bob.person_age)

class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month
        
    def birthday(self):
        self.age += 1

def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages 
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age
            
    return april_birthdays

def get_most_common_month(people):
    # TODO: Use the "months" dictionary to record counts of 
    # birthday months for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 
              'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
              'November':0, 'December':0}

    for person in people:
        months[person.birthday_month] += 1

    max_month = None
    max_value = 0
    for key in months.keys():
        if months[key] > max_value:
            max_value = months[key]
            max_month = key

    return max_month



def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
    ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
    months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))



test()


```