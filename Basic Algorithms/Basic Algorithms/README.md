# Basic Algorithms

## Binary search
Binary search is probably one of the most common algorithms that we all use without even realizing we are using it.

To help build a little intuition for how it works, let's first look at a classic game where the most efficient way to win is to use binary search.

## Guess the number
This notebook simulates a classic game where you have to guess a random number from within a certain range. Typically, you might have to guess a number from 1 to 10, and have three guesses to get the right answer.

In this case, you'll need to guess a random number between 1 and 100, and you will have 7 tries.

Try running it and playing a round or two. Notice that the game always tells you whether your guess was too high or too low. This information allows you to rule out some of the numbers (so that you don't waste time guessing those numbers).

With this fact in mind, try to make your guesses in the most efficient way you can. Specifically, try to make guesses that rule out the largest number of possibilities each time.

```python

import random

def guess_the_number(total_tries, start_range, end_range):
    if start_range > end_range:
        start_range, end_range = end_range, start_range
        
    random_number = random.randint(start_range, end_range)
    try_count = 0
    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"
    
    num_tries = 0
    while num_tries < total_tries:
        attempt = int(input("Guess the number: "))
        
        if attempt == random_number:
            print(success_message)
            return
        print(miss_message)
        if attempt < random_number:
            print("Go higher!")
        else:
            print("Go lower!")
        num_tries += 1
    print(failure_message)

total_tries = 7
start_range = 1
end_range = 100
guess_the_number(total_tries, start_range, end_range)


```

Obviously, there is some randomness involved in this game, so in some cases you may run out of tries before guessing correctly. However, if you use a binary search strategy, you'll find the number efficiently and win most of the time.

But before we look further into binary search, let's first look at an alternative: Linear search.

## Linear search
Suppose that you have a dictionary of words and that you need to look up a particular word in this dictionary. However, this dictionary is a pretty terrible dictionary, because the words are all in a scrambled order (and not alphabetical as they usually are). What search strategy would you use to find the definition you're looking for?

Because the words are in a random order, the best we can do is simply to go one by one, from the first page to the last page, in a sequential manner. Sounds tedious, right? This is called linear search. We have no idea about the order of the words, so we simply have to flip through the pages, one by one, until we find the word we are looking for.

With the example of the guessing game, you could use linear search there as well—by simply starting with 1 and guessing every number until you get to 100 (or rather, until you run out of tries and lose the game!).

## Back to binary search
Now let's consider a different scenario: Similar to the above, we have a dictionary and a word that we want to find in that dictionary. But this time, the dictionary is sorted in alphabetical order (just as you would expect from any decent dictionary). We still don't know what page our word is on, so we'll need to search for it—but the fact that the dictionary is sorted changes the strategy we should use.

Note: With a real dictionary, we might have some idea about the approximate location of a word. For example, if the word is "aardvark", we know it is going to be close to the beginning of the dictionary, while if it is "zebra", we know it will be close to the end. For the purposes of this example, we're going to ignore this kind of information.

Of the above options, the best strategy we can take is to open the dictionary in the middle.

Then, we do the following:

* Compare the target word with the words on this page.
* If the target word comes earlier (in terms of alphabetical order), then we discard the right half of the book. From now on, we will only search in the left half.
* Similarly, if the word comes later than the words on this page, then we discard the left half of the book. From now on, we will only search in the right half.

Whatever happens, we are guaranteed to be able to discard half of the search space in this first step alone.

Next, we repeat this process. We take the remaining half of the dictionary and we open it to the middle page. We then discard the left or right half, and repeat again. We continue this process, eliminating half of the search space at each step, until we find the target word. This is binary search.

Note that the word binary means "having two parts". Binary search means we are doing a search where, at each step, we divide the input into two parts. Also note that the data we are searching through has to be sorted.

Let's see what this would look like on a real data structure, such as an array:

# Binary Search
https://en.wikipedia.org/wiki/Binary_search_algorithm

https://youtu.be/0VN5iwEyq4c

In summary:

* Binary search is a search algorithm where we find the position of a target value by comparing the middle value with this target value.
* If the middle value is equal to the target value, then we have our solution (we have found the position of our target value).
* If the target value comes before the middle value, we look for the target value in the left half.
* Otherwise, we look for the target value in the right half.
We repeat this process as many times as needed, until we find the target value.

# Efficency of Binary Search

## Time complexity of binary search
How do we calculate the time complexity for binary search?

Check out the video below to get the gist, and then we'll walk through the process step-by-step after.

https://youtu.be/7WbRB7dSyvc


![Binary Search](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarysearch1.PNG "Binary Search")

![Binary Search](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarysearch_result_table.PNG "Binary Search")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath1.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath2.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath3.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath4.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath5.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchMath6.PNG "Binary Search Math")

![Binary Search Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchComplexity.PNG "Binary Search Math")

# Binary search practice
Let's get some practice doing binary search on an array of integers. We'll solve the problem two different ways—both iteratively and resursively.

Here is a reminder of how the algorithm works:

1. Find the center of the list (try setting an upper and lower bound to find the center)
2. Check to see if the element at the center is your target.
3. If it is, return the index.
4. If not, is the target greater or less than that element?
5. If greater, move the lower bound to just above the current center
6. If less, move the upper bound to just below the current center
7. Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).

## Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.

## Iterative solution
First, see if you can code an iterative solution (i.e., one that uses loops). If you get stuck, the solution is below.

## Iterative solution

```python

def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3
        
        mid_element = array[mid_index]
        
        if target == mid_element:                       # we have found the element
            return mid_index
        
        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half
        
        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half
    
    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


```

## Recursive Solution(Needs Debugging)

```python

def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
        
def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)


```

# Variations on Binary Search
Now that you've gone through the work of building a binary search function, let's take some time to try out a few exercises that are variations (or extensions) of binary search. We'll provide the function for you to start:

## Find First
The binary search function is guaranteed to return an index for the element you're looking for in an array, but what if the element appears more than once?

Consider this array:

[1, 3, 5, 7, 7, 7, 8, 11, 12]

Let's find the number 7:

Hmm...
Looks like we got the index 4, which is correct, but what if we wanted to find the first occurrence of an element, rather than just any occurrence?

Write a new function: find_first() that uses binary_search as a starting point.

Hint: You shouldn't need to modify binary_search() at all.

```python

def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple)) # Should return 3
print(find_first(9, multiple)) # Should return None


```

## Contains
The second variation is a function that returns a boolean value indicating whether an element is present, but with no information about the location of that element.

For example:

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
There are a few different ways to approach this, so try it out, and we'll share two solutions after.


![Binary Search Spoiler](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarySearchSpoiler.PNG "Binary Search Spoiler")

```python

def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


"""
# Loose wrapper for recursive binary search, returning True if the index is found and False if not
def contains(target, source):
    return recursive_binary_search(target, source) is not None

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False

"""

# Native implementation of binary search in the `contains` function.
def contains(target, source):
    if len(source) == 0:
        return False
    center = (len(source)-1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center+1:])
    else:
        return contains(target, source[:center])

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('c', letters)) ## True
print(contains('b', letters)) ## False



```









