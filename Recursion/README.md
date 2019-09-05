# Recursion
We're going to take a break from our tour of data structures in order to look at the concept of recursion. Recursion is going to be a useful tool for solving some of the problems we'll be tackling later on, and this is a good place to introduce it and get some practice using it with the data structures we're reviewing.

When you hear the terms recursion or recursive, this might remind you of the terms repetition and repetitive—and this is a good connection, because recursion does indeed involve repetition. However, recursion isn't just about repetition.

With recursion, we solve a problem by first solving smaller instances of the same problem. In practice, this often involves calling a function from within itself—in other words, we feed some input into the function, and the function produces some output—which we then feed back into the same function. And we continue to do this until we arrive at the solution.

https://youtu.be/_aI2Jch6Epk

## Call stack
https://en.wikipedia.org/wiki/Call_stack

![Recursion](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/recursion.PNG "Recursion")

```python

def power_of_2(n):
    if n == 0:
        return 1
    
    return 2 * power_of_2(n - 1)

print(power_of_2(5))


```
![Recursion2](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/recursion2.PNG "Recursion2")

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/callstack.PNG "Call Stack")


```python

def sum_integers(n):
    if n == 1:
        return 1
    
    return n + sum_integers(n -1)

print(sum_integers(3))



```

## Gotchas
When using recursion, there are a few things to look out for that you don't have to worry about when running a loop (iteratively). Let's go over a few of those items.

## Call Stack
We went over an example of the call stack when calling power_of_2(5) above. In this section, we'll cover the limitations of recursion on a call stack. Run the cell below to create a really large stack. It should raise the error RecursionError: maximum recursion depth exceeded in comparison.

```python
print(power_of_2(10000))

```

Python has a limit on the depth of recursion to prevent a <a href="https://en.wikipedia.org/wiki/Stack_overflow">stack overflow</a>. However, some compilers will turn <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions">tail-recursive functions</a> into an iterative loop to prevent recursion from using up the stack. Since Python's compiler doesn't do this, you'll have to watch out for this limit.

## Slicing
Let's look at recursion on arrays and how you can run into the problem of slicing the array. If you haven't heard the term slicing, it's the operation of taking a subset of some data. For example, the list a can be sliced using the following operation: a[start:stop]. This will return a new list from index start (inclusive) to index stop (exclusive).

Let's look at an example of a recursive function that takes the sum of all numbers in an array. For example, the array of [5, 2, 9, 11] would sum to 27 (5 + 2 + 9 + 11).

```python
def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr))

```

Looking at this, you might think it has a running time of O( 𝑛 ), but that isn't correct due to the slice operation array[1:]. This operation will take O( 𝑘 ) time to run where  𝑘  is the number of elements to copy. So, this function is actually O( 𝑘∗𝑛 ) running time complexity and O( 𝑘∗𝑛 ) space complexity.

To visualize this, let's plot the time it takes to slice.

```python

import matplotlib.pyplot as plt
import statistics
import time
%matplotlib inline

n_steps = 10
step_size = 1000000
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
times = []

# Calculate the time it takes for the slice function to run with different sizes of k
for array_size in array_sizes:
    start_time = time.time()
    big_array[:array_size]
    times.append(time.time() - start_time)

# Graph the results
plt.scatter(x=array_sizes, y=times)
plt.ylim(top=max(times), bottom=min(times))
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()



```

As you can see, it's linear time to slice.

Instead of slicing, we can pass the index for the element that we want to use for addition. That will give us the following function:

```python

def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))

```

That eliminates the need to do slicing. With the two different functions implemented, let's compare the running times.

```python

import matplotlib.pyplot as plt
import statistics
import time

n_steps = 10
step_size = 200
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
sum_array_times = []
sum_array_index_times = []

for array_size in array_sizes:
    subset_array = big_array[:array_size]
    
    start_time = time.time()
    sum_array(subset_array)
    sum_array_times.append(time.time() - start_time)
    
    start_time = time.time()
    sum_array_index(subset_array, 0)
    sum_array_index_times.append(time.time() - start_time)
    
    
plt.scatter(x=array_sizes, y=sum_array_times, label='sum_array')
plt.scatter(x=array_sizes, y=sum_array_index_times, label='sum_array_index')
plt.ylim(
    top=max(sum_array_times + sum_array_index_times),
    bottom=min(sum_array_times + sum_array_index_times))
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()


```
As you can see, the function sum_array is a polynomial and sum_array_index is linear as we predicted.

However, in our pursuit to use recursion we actually made things worse. Let's look at an iterative solution to this problem:

```python

def sum_array_iter(array):
    result = 0
    
    for x in array:
        result += x
    
    return result

arr = [1, 2, 3, 4]
print(sum_array_iter(arr))




```
The sum_array_iter function is a lot more straightforward than the two recursive functions, which is important. Second, to help ensure an answer that is correct and bug free, you generally want to pick the solution that is more readable. In some cases recursion is more readable and in some cases iteration is more readable. As you gain experience reading other people’s code, you’ll get an intuition for code readability.

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/factorial.PNG "Call Stack")

```python

# Code

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    
    # TODO: Write your recursive factorial function here
    if n == 0:
        return 1  # by definition of 0!
    return n * factorial(n-1)
    
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")

```

```python

# Solution
def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that us reversed of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

```

## Palindrome
A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome
The goal of this exercise is to use recursion to write a function is_palindrome that takes a string as input and checks whether that string is a palindrome. (Note that this problem can also be solved with a non-recursive solution, but that's not the point of this exercise.)

```python

# Solution

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        return (first_char == last_char) and is_palindrome(sub_input)

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")

```

## Permutation
Let's use recursion to help us solve this permutation problem:

Given a list of items, the goal is to find all of the permutations of that list. For example, if given a list like: ["apple", "water"], you could create two permuations from it. One in the form of the original input and one in the reversed order like so: ["water","apple"]

```python

# Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")

```

### Example 1:

* string = 'ab'
* output = ['ab', 'ba']

### Example 2:

* string = 'abc'
* output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

```python

# Solution
def permutations(string):
    return return_permutations(string, 0)
    
def return_permutations(string, index):
    # Base Case
    if index >= len(string):
        return [""]
    
    small_output = return_permutations(string, index + 1)
    
    output = list()
    current_char = string[index]
    
    # iterate over each permutation string received thus far
    # and place the current character at between different indices of the string
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)

```

## Keypad Combinations
A keypad on a cellphone has alphabets for all numbers between 2 and 9.

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

ad, ae, af, bd, be, bf, cd, ce, cf

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise, if the user types 32, the order would be

da, db, dc, ea, eb, ec, fa, fb, fc

Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.

```python

def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    output = list()
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")

# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)

# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)

# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)

# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)

input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)

```

## Problem Statement
Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.

Note: The procedure must not change the input list itself.

```python

def deep_reverse(arr):
    pass

def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def deep_reverse(arr):
    """
    Function to deep_reverse an input list
    """
    return deep_reverse_func(arr, 0)

def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    """
    # Base Case
    if index == len(arr):
        return list()
    
    output = deep_reverse_func(arr, index + 1)
    
    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]
        
    output.append(to_append)
    return output

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)



```

## VISUALIZE CODE AND GET LIVE HELP(Learn Python, Java, C, C++, JavaScript, and Ruby)
http://pythontutor.com/


## Call stacks and recursion
In this notebook, we'll take a look at call stacks, which will provide an opportunity to apply some of the concepts we've learned about both stacks and recursion.

## What is a call stack?
When we use functions in our code, the computer makes use of a data structure called a call stack. As the name suggests, a call stack is a type of stack—meaning that it is a Last-In, First-Out (LIFO) data structure.

So it's a type of stack—but a stack of what, exactly?

Essentially, a call stack is a stack of frames that are used for the functions that we are calling. When we call a function, say print_integers(5), a frame is created in memory. All the variables local to the function are created in this memory frame. And as soon as this frame is created, it's pushed onto the call stack.

The frame that lies at the top of the call stack is executed first. And as soon as the function finishes executing, this frame is discarded from the call stack.

## An example
Let's consider the following function, which simply takes two integers and returns their sum

```python

def add(num_one, num_two):
    output = num_one + num_two
    return output

result = add(5, 7)
print(result)

```

Before understanding what happens when a function is executed, it is important to remind ourselves that whenever an expression such as product = 5 * 7 is evaluated, the right hand side of the = sign is evaluted first. When the right-hand side is completely evaluated, the result is stored in the variable name mentioned in the left-hand side.

When Python executes line 1 in the previous cell (result = add(5, 7)), the following things happen in memory:

A frame is created for the add function. This frame is then pushed onto the call stack. We do not have to worry about this because Python takes care of this for us.
Next, the parameters num_one and num_two get the values 5 and 7, respectively
If we run this code in Python tutor website <a href="http://pythontutor.com/">http://pythontutor.com/)</a>, we can get a nice visualization of what's happening "behind the scenes" in memory:

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/callstack1.PNG "Call Stack")

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/callstack2.PNG "Call Stack")

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/callstack3.PNG "Call Stack")
