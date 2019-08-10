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


```