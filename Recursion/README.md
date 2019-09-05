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

Now the next question is how does this behave like a stack? The answer is pretty simple. We know that a stack is a Last-In First-Out (LIFO) structure, meaning the latest element inserted in the stack is the first to be removed.

You can play more with such "behind-the-scenes" of code execution on the Python tutor website: http://pythontutor.com/

## Another example
Here's another example. Let's say we have a function add() which adds two integers and then prints a custom message for us using the custom_print()

```python

def add(num_one, num_two):
    output = num_one + num_two
    custom_print(output, num_one, num_two)
    return output

def custom_print(output, num_one, num_two):
    print("The sum of {} and {} is: {}".format(num_one, num_two, output))
    
result = add(5, 7)    

```

## Call Stack and Recursion
## Problem Statement
Consider the following problem:

Given a positive integer n, write a function, print_integers, that uses recursion to print all numbers from n to 1.

For example, if n is 4, the function shuld print 4 3 2 1.

If we use iteration, the solution to the problem is simple. We can simply start at 4 and use a loop to print all numbers till 1. However, instead of using an interative approach, our goal is to solve this problem using recursion.

Now let's consider what happens in the call stack when print_integers(5) is called.

* As expected, a frame will be created for the print_integers() function and pushed onto the call stack.

* Next, the parameter n gets the value 5.

* Following this, the function starts executing. The base condition is checked. For n = 5, the base case is False, so we move forward and print the value of n.

* In the next line, print_integers() is called again. This time it is called with the argument n - 1. The value of n in the current frame is 5. So this new function call takes place with value 4. Again, a new frame is created. Note that for every new call a new frame will be created. This frame is pushed onto the top of the stack.

* Python now starts executing this frame. Again the base case is checked. It's False for n = 4. Following this, the n is printed and then print_integers() is called with argument n - 1 = 3.

* The process keep on like this until we hit the base case. When n <= 0, we return from the frame without calling the function print_integers() again. Because we have returned from the function call, the frame is discarded from the call stack and the next frame resumes execution right after the line where we left off.

## Problem Statement
Previously, we considered the following problem:

Given a positive integer n, write a function, print_integers, that uses recursion to print all numbers from n to 1.

For example, if n is 4, the function shuld print 4 3 2 1.

Our solution was:

![Print Integers](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/printintegers.PNG "Print Integers")

Note that in Python, the stack is displayed in an "upside down" manner. This can be seen in the illustration above—the last frame (i.e. the frame with n = 0) lies at the top of the stack (but is displayed last here) and the first frame (i.e., the frame with n = 5) lies at the bottom of the stack (but is displayed first).

But don't let this confuse you. The frame with n = 0 is indeed the top of the stack, so it will be discarded first. And the frame with n = 5 is indeed at the bottom of the stack, so it will be discarded last.

We define time complexity as a measure of amount of time it takes to run an algorithm. Similarly, the time complexity of our function print_integers(5), would indicate the amount of time taken to exceute our function print_integers. But notice how when we call print_integers() with a particular value of n, it recursively calls itself multiple times.

In other words, when we call print_integers(n), it does operations (like checking for base case, printing number) and then calls print_integers(n - 1).

Therefore, the overall time taken by print_integers(n) to execute would be equal to the time taken to execute its own simple operations and the time taken to execute print_integers(n - 1).

Let the time taken to execute the function print_integers(n) be 𝑇(𝑛). And let the time taken to exceute the function's own simple operations be represented by some constant, 𝑘.

In that case, we can say that

𝑇(𝑛)=𝑇(𝑛−1)+𝑘

where 𝑇(𝑛−1) represents the time taken to execute the function print_integers(n - 1).

Similarly, we can represent 𝑇(𝑛−1) as

𝑇(𝑛−1)=𝑇(𝑛−2)+𝑘

We can see that a pattern is being formed here:

𝑇(𝑛)       =𝑇(𝑛−1)+𝑘

𝑇(𝑛−1)=𝑇(𝑛−2)+𝑘

𝑇(𝑛−2)=𝑇(𝑛−3)+𝑘

𝑇(𝑛−3)=𝑇(𝑛−4)+𝑘

.
.
.
.
.
.

𝑇(2)=𝑇(1)+𝑘

𝑇(1)=𝑇(0)+𝑘

𝑇(0)=𝑘1

Notice that when n = 0 we are only checking the base case and then returning. This time can be represented by some other constant,  𝑘1 .

If we add the respective left-hand sides and right-hand sides of all these equations, we get:

𝑇(𝑛)=𝑛𝑘+𝑘1
 
We know that while calculating time complexity, we tend to ignore these added constants because for large input sizes on the order of  105 , these constants become irrelevant.

Thus, we can simplify the above to:

𝑇(𝑛)=𝑛𝑘
 
We can see that the time complexity of our function print_integers(n) is a linear function of  𝑛 . Hence, we can say that the time complexity of the function is  𝑂(𝑛) .

## how to calculate binary search complexity
https://stackoverflow.com/questions/8185079/how-to-calculate-binary-search-complexity

Let's try to analyze the time complexity of the recursive algorithm for binary search by finding out the recurrence relation.

Our binary_search() function calls the binary_search_func() function. So the time complexity of the function is entirely dependent on the time complexity of the binary_search_func().

The input here is an array, so our time complexity will be determined in terms of the size of the array.

Like we did earlier, let's say the time complexity of binary_search_func() is a function of the input size, n. In other words, the time complexity is 𝑇(𝑛).

Also keep in mind that we are usually concerned with the worst-case time complexity, and that is what we will calculate here. In the worst case, the target value will not be present in the array.

In the binary_search_func() function, we first check for the base case. If the base case does not return True, we calculate the mid_index and then compare the element at this mid_index with the target values. All the operations are independent of the size of the array. Therefore, we can consider all these independent operations as taking a combined time, 𝑘.

Apart from these constant time operations, we do just one other task. We either make a call on the left-half of the array, or on the right half of the array. By doing so, we are reducing the input size by 𝑛/2.

Note: Remember that we usually consider large input sizes while calculating time complexity; there is no significant difference between 105 and (105+1).

Thus, our new function call is only called with half the input size. We said that 𝑇(𝑛) was the time complexity of our original function. The time complexity of the function when called with half the input size will be 𝑇(𝑛/2).

Therefore:

𝑇(𝑛)=𝑇(𝑛/2)+𝑘
Similarly, in the next step, the time complexity of the function called with half the input size would be:

𝑇(𝑛/2)=𝑇(𝑛/4)+𝑘
We can now form similar equations as we did for the last problem:

𝑇(𝑛)   =𝑇(𝑛/2)+𝑘

𝑇(𝑛/2)=𝑇(𝑛/4)+𝑘

𝑇(𝑛/4)=𝑇(𝑛/8)+𝑘

𝑇(𝑛/8)=𝑇(𝑛/16)+𝑘

.
.
.
.
.
.
𝑇(4)=𝑇(2)+𝑘

𝑇(2)=𝑇(1)+𝑘

𝑇(1)=𝑇(0)+𝑘1 (1)

𝑇(0)=𝑘1

(1) If we have only one element, we go to 0 elements next

From our binary search section, we know that it takes 𝑙𝑜𝑔(𝑛) steps to go from 𝑇(𝑛) to 1. Therefore, when we add the corresponding left-hand sides and right-hand sides, we can safely say that:

𝑇(𝑛)=𝑙𝑜𝑔(𝑛)∗𝑘+𝑘1

As always, we can ignore the constant. Therefore:

𝑇(𝑛)=𝑙𝑜𝑔(𝑛)∗𝑘

Thus we see that the time complexity of the function is a logarithmic function of the input, 𝑛. Hence, the time complexity of the recursive algorithm for binary search is 𝑙𝑜𝑔(𝑛).

```python
def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)

def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(arr, 5))

```

## Tower of Hanoi
Problem Statement
The Tower of Hanoi is a puzzle where we have three rods and n disks. The three rods are:

1. source
2. destination
3. auxiliary
Initally, all the n disks are present on the source rod. The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod. However, there are some rules according to which this has to be done:

1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.
You will be given the number of disks num_disks as the input parameter.

For example, if you have num_disks = 3, then the disks should be moved as follows:

    1. move disk from source to auxiliary
    2. move disk from source to destination
    3. move disk from auxiliary to destination
You must print these steps as follows:

    S A
    S D
    A D
Where S = source, D = destination, A = auxiliary

```python

# Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')


num_disks = 4
tower_of_Hanoi(num_disks)


"""

Compare your results with the following test cases
num_disks = 2

  solution 
          S A
          S D
          A D
num_disks = 3

  solution 
          S D
          S A
          D A
          S D
          A S
          A D
          S D
num_disks = 4

  solution
          S A
          S D
          A D
          S A
          D S
          D A
          S A
          S D
          A D
          A S
          D S
          A D
          S A
          S D
          A D



"""


```

## Problem statement
In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.

## Example 1

number = 123
codes_possible = ["aw", "abc", "lc"]
Explanation: The codes are for the following number:

1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"

## Example 2

number = 145
codes_possible = ["ade", "ne"]
Return the codes in a list. The order of codes in the list is not important.

Note: you can assume that the input number will not contain any 0s

```python

# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    return output

def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)




```

## Problem Statement
Given an integer array, find and return all the subsets of the array. The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

Note: An empty set will be represented by an empty list

Example 1

arr = [9]

output = [[]
          [9]]
Example 2

arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]

```python

# Solution
def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    

arr = [9]
solution = [[], [9]]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 8, 9, 8]
solution = [[],
[8],
[9],
[9, 8],
[8],
[8, 8],
[8, 9],
[8, 9, 8],
[9],
[9, 8],
[9, 9],
[9, 9, 8],
[9, 8],
[9, 8, 8],
[9, 8, 9],
[9, 8, 9, 8]]

test_case = [arr, solution]
test_function(test_case)


```

## Problem Statement
Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps? Write a recursive function to solve the problem.

Example:

n = 3
output = 4
The output is 4 because there are four ways we can climb the staircase:

1. 1 step +  1 step + 1 step
2. 1 step + 2 steps 
3. 2 steps + 1 step
4. 3 steps

```python

# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)


```

## Problem statement
Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 4] and target = 5, output = 3

For arr = [1, 2, 5, 5, 4] and target = 7, output = -1

```python

# Solution
def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    
    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)

def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 5, 5, 4]
target = 5
solution = 3
test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 2, 5, 5, 4]
target = 7
solution = -1
test_case = [arr, target, solution]
test_function(test_case)

arr = [91, 19, 3, 8, 9]
target = 91
solution = 0
test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5
test_case = [arr, target, solution]
test_function(test_case)

```