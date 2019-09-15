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
![New Tweet View](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/quickSort.PNG "New Tweet View")
