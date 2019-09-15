# Sorting Algorithms

## Intro to Sorting
https://youtu.be/Z6yuIen71zM

## Bubble Sort
https://youtu.be/h_osLG3GmjE

## Efficiency of Bubble Sort
https://youtu.be/KddkHygi7is

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort1.PNG "Bubble Sort")

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort2.PNG "Bubble Sort")

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort3.PNG "Bubble Sort")



## Bubble Sort Exercises
Now that you know how about bubble sort works, you'll implement bubble sort for two exercises.

### Exercise 1
Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.

```python

def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this
    print(l)

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")



```

### Exercise 2
Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest.

```python

def bubble_sort_2(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)
    print(l)

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

```

## Merge Sort
https://youtu.be/K916wfSzKxE

## Efficiency of Merge Sort
https://youtu.be/HKiK5Y-YSkks

![Merge Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/mergesort.PNG "Merge Sort")

![Merge Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/mergesort2.PNG "Merge Sort")


MergeSort is a divide and conquer algorithm that divides a list into equal halves until it has two single elements and then merges the sub-lists until the entire list has been reassembled in order.

## Divide
Our MergeSort code will focus first on the divide portion of the algorithm. If the list we receive has only a single element in it, the list can be considered sorted and we can return immediately. This is our recursion base case. If we have more than 1 element we need to split the list into equal halves and call MergeSort again for each half.

## Conquer
Once you have split the list down to single elements, your mergesort will start merging lists, in order, until you have reassembled the entire list in order.

![Merge Sort Design](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/mergesortdesign.PNG "Merge Sort Design")

## Divide
We can use python's // operator to find a midpoint. If items's length is even, we will have the midpoint. If items's length is odd, we will have one half larger by one.


```python

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1
     
    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]
        
    # return the ordered, merged list
    return merged

# Test this out
merged = merge([1,3,7], [2,5,6])
print(merged)

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))


```

## Counting Inversions
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

Here are some examples:

* [0,1] has 0 inversions
* [2,1] has 1 inversion (2,1)
* [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
* [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

 Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.

## Problem statement
Write a function, count_inversions, that takes an array (or Python list) as input, and returns a count of the total number of inversions present in the input.

Mergesort provides an efficient way to solve this problem.

```python

def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    
    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)
    
    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer
    
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)           # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)


```


## Case Specific Sorting of Strings
## Problem statement
Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort, that sorts uppercase and lowercase letters separately, such that if the  𝑖 th place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.

For example:
Input: fedRTSersUXJ
Output: deeJRSfrsTUX

```python

def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0
    
    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:       # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break
            
    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)

def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]
    
    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)




```

## QuickSort
https://youtu.be/kUon6854joI

## QuickSort Efficiency
https://youtu.be/TH5RT5XcdAo


![Quick Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/quicksort2.PNG "Quick Sort")


## Quick Sort Walkthrough

Like MergeSort, QuickSort is a divide-and-conquer algorithm. We need to pick a pivot, then sort both sublists that are created on either side of the pivot. Similar to the video, we'll follow the convention of picking the last element as the pivot.

Start with our unordered list of items:

```python

items = [8, 3, 1, 7, 0, 10, 2]

```

Let's sketch out what a first iteration would look like.

We can use len to grab the pivot value, but in order to sort in-place we'll also want the index of the pivot.

```python

pivot_index = len(items) - 1
pivot_value = items[pivot_index]

```

Because we plan on sorting in-place, we want to iterate through the items to the left of our pivot (left_items). When they're larger than pivot_value though, we will not increment our position through left_items, but instead change pivot_index. We'll know we're done with this pass when pivot_index and left_items index are equal.

```python

left_index = 0

while (pivot_index != left_index):
    
    item = items[left_index]
    
    if item <= pivot_value:
        left_index += 1
        continue
    
    # Place the item before the pivot at left_index
    items[left_index] = items[pivot_index - 1]
    # Shift pivot one to the left
    items[pivot_index - 1] = pivot_value
    # Place item at pivot's previous location
    items[pivot_index] = item
    # Update pivot_index
    pivot_index -= 1

print(items)
        


```

You should see:

[0, 1, 2, 7, 3, 10, 8]
When our loop terminated, we knew everything to the left of our pivot was less than pivot, and everything to the right of our pivot was greater than pivot. Great! Now we need to do that again for the sublists that are left and right of pivot's final location.

We can do that by abstracting our above code to a function, just passing the list of items as a parameter.

```python

def sort_a_little_bit(items):
    left_index = 0
    pivot_index = len(items) - 1
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
        
items = [8, 3, 1, 7, 0, 10, 2]
sort_a_little_bit(items)
print(items)


```

Now what would it require to recurse on this? We want to take the result of that iteration and act on it. So first off, we see that in order to call the function again, we need to communicate the final pivot_index value. And then with that, we can mark off segments of the list and have our function operate on less than the entire list. So let's change our function to accept the indices it should stay within, and return the pivot_index.

```python

def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

items = [8, 3, 1, 7, 0, 10, 2]
pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
print(items)
print('pivot index %d' % pivot_index)

```


Almost there! Let's create another function, the recursive function we want, that uses this. And then we'll have our top level definition of quicksort call it with our initial parameters. But we need a way to know if we're done! We'll use the indices to see if they demark a list of more than one item. If the demarked sublist is 0 or 1 item, we know it's already sorted.


```python

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)


It's a good idea to test a few more scenarios. Does it work with an even number of items? What if they're already sorted?

```python

items = [1, 0]
quicksort(items)
print(items)

items = [96, 97, 98]
quicksort(items)
print(items)



```


### Mission Accomplished!

## Heapsort

A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.

The main steps in a heapsort are:

1. Convert the array into a maxheap (a complete binary tree with decreasing values)
2. Swap the top element with the last element in the array (putting it in it's correct final position)
3. Repeat with arr[:len(arr)-1] (all but the sorted elements)

## Visualization of a heapsort
https://commons.wikimedia.org/wiki/File:Heapsort-example.gif

## Problem statement
In the cell below, see if you can code a heapsort function that takes an array (or Python list) and performs a heapsort on it. You will have to complete the heapify

```python

# Solution

def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
    
        heapify(arr, n, largest_index) 
        
def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)

```

## Pair Sum

## Problem Statement
Given an input array and a target value (integer), find two values in the array whose sum is equal to the target value. Solve the problem without using extra space. You can assume the array has unique values and will never have more than one solution.

```python

def pair_sum(arr, target):
    # sort the list
    arr.sort()
    
    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:       # sum < target ==> shift front pointer forward
            front_index += 1 
        else:
            back_index -= 1               # sum > target ==> shift back pointer backward

    return [None, None]

def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")



input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)


```

## Sort 0, 1, 2

```python

def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:           
            input_list[front_index] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1

def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)


```


