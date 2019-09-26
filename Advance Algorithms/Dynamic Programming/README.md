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