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


