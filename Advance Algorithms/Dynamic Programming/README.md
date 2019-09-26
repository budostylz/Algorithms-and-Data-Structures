# Dynamic Programming

## Knapsack Problem
https://youtu.be/-xRKazHGtjU

## Knapsack Problem Step by Step
https://youtu.be/8LusJS5-AGo

## Dynamic Programming
https://youtu.be/VQeFcG9pjJU

## Smarter Approach
https://youtu.be/J7S3CHFBZJA

## Knapsack Problem

Now that you saw the dynamic programming solution for the knapsack problem, it's time to implement it. Implement the function max_value to return the maximum value given the items (items) and the maximum weight of the knapsack (knapsack_max_weight). The items variable is the type Item, which is a named tuple.


```python

import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]



tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])





```

## Longest Common Subsequence

In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text). In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence or LCS.

    The Longest Common Subsequence is the longest string of letters that are the same between to strings.

A short example:

    * For two input strings, A and B
        * A = 'ABCD'
        * B = 'BD'
    * The LCS is 'BD', which has a length of 2 characters

![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Dynamic%20Programming/longest_common_subsequence1.PNG "Longest Common Subsequence")

![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Dynamic%20Programming/longest_common_subsequence2.PNG "Longest Common Subsequence")

![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Dynamic%20Programming/longest_common_subsequence3.PNG "Longest Common Subsequence")

![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Dynamic%20Programming/longest_common_subsequence4.PNG "Longest Common Subsequence")


## Calculate the longest common subsequence

Implement the function lcs; this should calculate the longest common subsequence of characters between two strings.

```python

def lcs(string_a, string_b):
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    return lookup_table[-1][-1]

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')


# The time complexity of the above implementation
# is dominated by the two nested loops,
# which give us an O(N^2) time complexity.



```

## Longest Palindromic Subsequence

In this notebook, you'll be tasked with finding the length of the Longest Palindromic Subsequence (LPS) given a string of characters.

As an example:

    * With an input string, ABBDBCACB
    * The LPS is BCACB, which has length = 5

In this notebook, we'll focus on finding an optimal solution to the LPS task, using dynamic programming. There will be some similarities to the Longest Common Subsequence (LCS) task, which is outlined in detail in a previous notebook. It is recommended that you start with that notebook before trying out this task.

## Hint

<strong>Storing pre-computed values</strong>s

The LPS algorithm depends on looking at one string and comparing letters to one another. Similar to how you compared two strings in the LCS (Longest Common Subsequence) task, you can compare the characters in just one string with one another, using a matrix to store the results of matching characters.

For a string on length n characters, you can create an n x n matrix to store the solution to subproblems. In this case, the subproblem is the length of the longest palindromic subsequence, up to a certain point in the string (up to the end of a certain substring).

It may be helpful to try filling up a matrix on paper before you start your code solution. If you get stuck with this task, you may look at some example matrices below (see the section titled Example matrices), before consulting the complete solution code.


![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Dynamic%20Programming/LongestPalindromicSubsequence.PNG "Longest Common Subsequence")




## The matrix rules

You can efficiently fill up this matrix one cell at a time. Each grid cell only depends on the values in the grid cells that are directly on bottom and to the left of it, or on the diagonal/bottom-left. The rules are as follows:

    * Start with an n x n matrix where n is the number of characters in a given string; the diagonal should all have the value 1 for the base case, the rest can be zeros.
    * As you traverse your string:
        * If there is a match, fill that grid cell with the value to the bottom-left of that cell plus two.
        * If there is not a match, take the maximum value from either directly to the left or the bottom cell, and carry that value over to the non-match cell.
    * After completely filling the matrix, the top-right cell will hold the final LPS length.

```python

## Solution

# imports for printing a matrix, nicely
import pprint
pp = pprint.PrettyPrinter()

# complete LPS solution
def lps(input_string): 
    n = len(input_string) 
  
    # create a lookup table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # strings of length 1 have LPS length = 1
    for i in range(n): 
        L[i][i] = 1 
    
    # consider all substrings
    for s_size in range(2, n+1): 
        for start_idx in range(n-s_size+1): 
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]); 
  
    # debug line
    # pp.pprint(L)
    
    return L[0][n-1] # value in top right corner of matrix


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)




```



