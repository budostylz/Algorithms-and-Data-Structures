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

## Problem statement
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).

The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .

```python

def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)
    
    # search last occurence
    last_index =  find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return  -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)


```
# Trie
https://en.wikipedia.org/wiki/Trie#targetText=In%20computer%20science%2C%20a%20trie,the%20keys%20are%20usually%20strings.

You've learned about Trees and Binary Search Trees. In this notebook, you'll learn about a new type of Tree called Trie. Before we dive into the details, let's talk about the kind of problem Trie can help with.

Let's say you want to build software that provides spell check. This software will only say if the word is valid or not. It doesn't give suggested words. From the knowledge you've already learned, how would you build this?

The simplest solution is to have a hashmap of all known words. It would take O(1) to see if a word exists, but the memory size would be O(n*m), where n is the number of words and m is the length of the word. Let's see how a Trie can help decrease the memory usage while sacrificing a little on performance.

## Basic Trie
Let's look at a basic Trie with the following words: "a", "add", and "hi"

```python

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


```

You can lookup a word by checking if word_end is True after traversing all the characters in the word. Let's look at the word "hi". The first letter is "h", so you would call basic_trie['h']. The second letter is "i", so you would call basic_trie['h']['i']. Since there's no more letters left, you would see if this is a valid word by getting the value of word_end. Now you have basic_trie['h']['i']['word_end'] with True or False if the word exists.

In basic_trie, words "a" and "add" overlapp. This is where a Trie saves memory. Instead of having "a" and "add" in different cells, their characters treated like nodes in a tree. Let's see how we would check if a word exists in basic_trie.

```python

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie
    
    for char in word:
        if char not in current_node:
            return False
        
        current_node = current_node[char]
    
    return current_node['word_end']


# Test words
test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))



```

The is_word starts with the root node, basic_trie. It traverses each character (char) in the word (word). If a character doesn't exist while traversing, this means the word doesn't exist in the trie. Once all the characters are traversed, the function returns the value of current_node['word_end'].

You might notice the function is_word is similar to a binary search tree traversal. Since Trie is a tree, it makes sense that we would use a type of tree traversal. Now that you've seen a basic example of a Trie, let's build something more familiar.

## Trie Using a Class
Just like most tree data structures, let's use classes to build the Trie. Implement two functions for the Trie class below. Implement add to add a word to the Trie. Implement exists to return True if the word exist in the trie and False if the word doesn't exist in the trie.

```python

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))




```

## Trie using Defaultdict (Optional)
This is an optional section. Feel free to skip this and go to the next section of the classroom.

A cleaner way to build a trie is with a Python default dictionary. The following TrieNod class is using collections.defaultdict instead of a normal dictionary.

```python

import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

            current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word

# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')




```

The Trie data structure is part of the family of Tree data structures. It shines when dealing with sequence data, whether it's characters, words, or network nodes. When working on a problem with sequence data, ask yourself if a Trie is right for the job.

# Heaps
https://youtu.be/M3B0UJWS_ag

## Heapify
https://youtu.be/CAbDbiCfERY

## Heap Implementation
https://youtu.be/2LAdml6_pDY

# Priority Queues - Intuition
Consider the following scenario -

A doctor is working in an emergency wing at a hospital. When patients come in, a nurse checks their symptoms and based on the severity of the illness, sends them to the doctor. For e.g. a guy who has had an accident is sent before someone who has come with a runny nose. But there is a slight problem. There is only one nurse and only one doctor. In the amount of time nurse takes to check the symptoms, the doctor has to work alone with the patients, hurting their overall productivity.

You are a ninja programmer. The doctor comes to you for help. Your job is to write a small software in which patients will enter their symptoms and will receive a priority number based on their illness. The doctor has given you a list of common ailments, and the priority in which he would prefer seeing them. How would you solve the priority problem?

## Priority Queues
Like the name suggests, a priority queue is similar to a regular queue, except that each element in the queue has a priority associated with it. A regular queue is a FIFO data structure, meaning that the first element to be added to the queue is also the first to be removed.

With a priority queue, this order of removal is instead based on the priority. Depending on how we choose to set up the priority queue, we either remove the element with the most priority, or an element of the least priority.

For the sake of discussion, let's focus on removing the element of least priority for now.

## Functionality
If we were to create a PriorityQueue class, what methods would it need to have?

Here are the two key methods:

* insert - insert an element
* remove - remove an element
And we can also add the same utility methods that we had in our regular Queue class:

* front - returns the element at the front of the queue
* size - returns the number of elements present in the queue
* is_empty - returns True if there are no elements in the queue, and False otherwise
As part of this functionality, we will need a way of assigning priorities to the items.

A very common way to solve the patient-doctor problem mentioned above would be to assign each ailment a priority. For e.g.

* A running nose may be assigned priority 1
* Fever may be assigned 2
* Accident may get a priority 10

You will find this theme recurring in all of programming. We use numbers to effectively represent data.

For the sake of simplicity, let's only consider integers here. Let us assume a scenario where we get integers as input and we assign a priority on how large / small they are. Let us say the smaller the number, the smaller its priority. So, in our simplified version of the problem statement the value of the integer serves as a priority.

Our goal is to create a queue where the element with the lowest priority is removed first. Therefore, the remove method will remove the smallest number from the priority queue. Thus, the largest number will be the last to be removed from the priority queue and the smallest number will be the first to be removed.

## How should we implement it?
What we've described above is just the abstract characteristics that we expect from this data structure. As with stacks and queues (and other abstract data types), there is more than one way that we could implement our priority queue such that it would exhibit the above behaviors.

However, not all implementations are ideal. When we implemented a regular queue earlier, you may remember the enqueue and dequeue methods had a time complexity of  𝑂(1) . Similarly, we would like the insert and remove methods on our priority queue to be fast.

So, what underlying structure should we use to implement the priority queue such that it will be as efficient as possible? Let's look at some different structures and consider the pros and cons.

## Arrays
Earlier, we saw that one way to implement a queue was by using an array. We could do a similar thing for priority queues. We could use the array to store our data.

Insertion in an array is very fast. Unless the array is full, we can do it in O(1) time.

Note: When the array is full, we will simply create a new array and copy all the elements from our old array to new array. It's exactly similar to what we do for our queue's implementation using arrays.

What about removal? We always want to remove the smallest or highest priority data from the array, depending on if this is a max-heap or min-heap. In the worst case, we will have to search the entire array, which will take O(n) time. Thus, to remove the element, the time complexity would be O(n).

This also creates an additional problem for us. The index from which we removed the element is now empty. We cannot leave empty indices in our array. Over the course of operations, we will be wasting a lot of space if we did that.

Therefore, insertion no longer happens in O(1) time. Rather, every time we insert, we will have to look for these empty indices and put our new element in the first empty index we find. In the worst case, this also takes O(n) time. Therefore, our time complexity with arrays (for both insertion and removal) would be O(n).

## LinkedList
Insertion is very easy in a linked list. If we maintain a variable to keep track of the tail of the linked list, then we can simply add a new node at this location. Thus, insertion takes O(1) time.

For removal, we will have to traverse the entire list and find the smallest element, which will require O(n) time.

Note that with linked lists, unlike arrays, we do not have to worry about empty indices.

A linked linked certainly seems to be a better option than an array. Although they have the same time complexity for removal, the time complexity for insertion is better.

## HashMap
The same problem lies in HashMap as well. We can insert in O(1) time. Although, we can remove an element from a HashMap in O(1) time but we have to first search for the smallest element in the map. This will again take O(n) time. Therefore, the time complexity of remove is O(n) for hashmaps.

## Binary Search Trees
Binary Search Trees are laid out according to the value of the node that we want to insert. All elements greater than the root go to the right of the root, and all elements smaller than the root go to the left of the root.

If we assume that our Binary Search tree is balanced, insertion would require O(h) time in the worst case. Similarly, removal would also require O(h) time. Here h is the height of the binary search tree.

![Binary Search Tree](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarysearchtree1.PNG "Binary Search Tree")

A Binary Tree is called a Balanced Binary Tree when the difference between the heights of it's left subtree and right subtree do not differ by more than one. Additionally, to be balanced, all the subtrees of the binary tree must also be balanced.

For a balanced tree, we can safely approximate the height of the tree h to log(n). Thus, both insertion and removal require O(log(n)) time in a binary search tree.

However, in the worst case, our binary search tree might just be a sequential list of nodes (stretching to the right or to the left). Consider the following tree:

![Binary Search Tree](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/binarysearchtree2.PNG "Binary Search Tree")

In such a scenario the binary search tree effectively turns into a linked list. In this case, the time complexity would be O(n)

To avoid this situation, we would need a self-balancing tree which incure additional complexity.

We could use any of the above data structures to implement our priority queue—and they would work, in the sense that they would exhibit the outward behavior we expect in a priority queue.

However, none of them acheived our goal of having  𝑂(1)  time complexity for both insert and remove. To do that, we will need to explore something new: A heap.

## Full v.s. Complete Binary Trees
https://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html#targetText=A%20full%20binary%20tree%20(sometimes,as%20far%20left%20as%20possible.

## Heaps
A heap is a data structure with the following two main properties:

1. Complete Binary Tree
2. Heap Order Property

1. Complete Binary Tree - Like the name suggests we use a binary tree to create heaps. A complete binary tree is a special type of binary tree in which all levels must be filled except for the last level. Moreover, in the last level, the elements must be filled from left to right.

![Complete Binary Trees](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/completebinarytree1.PNG "Complete Binary Trees")

A. is a complete binary tree. Notice how every level except the last level is filled. Also notice how the last level is filled from left to right.

![Complete Binary Trees](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/completebinarytree2.PNG "Complete Binary Trees")

B. is not a complete binary tree. Although evey level is filled except for the last level. Notice how the last level is not filled from left to right. 25 does not have any right node and yet there is one more node (9) in the same level towards the right of it. It is mandatory for a complete binary tree to be filled from left to right.

![Complete Binary Trees](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/completebinarytree3.PNG "Complete Binary Trees")

C. is also not a binary tree. Notice how the second level is not completely filled and yet we have elements in the third level. The right node of `10` is empty and yet we have nodes in the next level.

<strong>Heap Order Property</strong> - Heaps come in two flavors
* Min Heap
* Max Heap

* Min Heap - In the case of min heaps, for each node, the parent node must be smaller than both the child nodes. It's okay even if one or both of the child nodes do not exists. However if they do exist, the value of the parent node must be smaller. Also note that it does not matter if the left node is greater than the right node or vice versa. The only important condition is that the root node must be smaller than both it's child nodes
* Max Heap - For max heaps, this condition is exactly reversed. For each node, the value of the parent node must be larger than both the child nodes.

Thus, for a data structure to be called a Heap, it must satisfy both of the above properties.

1. It must be a complete binary tree
2. It must satisfy the heap order property. If it's a min heap, it must satisfy the heap order property for min heaps. If it's a max heap, it should satisfy the heap order property for max heaps.

## Complete Binary Tree
Let's go back to our complete binary tree A.

![Complete Binary Trees](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/completebinarytree1.PNG "Complete Binary Trees")

If we have to insert one more node, where should the next node go? Because A. is a complete binary tree, the next node can only go as the left node of 15.

![Complete Binary Trees](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/completebinarytree4.PNG "Complete Binary Trees")

Similarly, let's look back A. again. If we have to delete a node from A., which node should we delete? Again, to ensure that our tree remains a complete binary tree even after deleting a node, we can only remove 9.

Thus, we know which node to remove and where to insert a new node. Notice that both of these operations do not depend upon values of other nodes. Rather, both insert and remove operations on a complete binary tree depend upon the position of the last inserted node.

## Non-Linear Inequalities
https://github.com/budostylz/Mathematics/tree/master/Algebra-PreCal/Intermediate%20Algebra/Non-Linear%20Inequalities

![Heap Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/heapmath2.PNG "Heap Math")


![Heap Math](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Basic%20Algorithms/heapmath.PNG "Heap Math")






































