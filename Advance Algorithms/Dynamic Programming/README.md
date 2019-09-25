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

## Storing pre-computed values

The LCS algorithm depends on looking at two strings and comparing them letter by letter. You can solve this problem in multiple ways. You can iterate through each letter in the strings and compare them, adding to your value for LCS as you go.

The method I recommend for implementing an efficient LCS algorithm is: using a matrix and dynamic programming. Recall that dynamic programming is all about breaking a larger problem into a smaller set of subproblems, and building up a complete result without having to repeat any subproblems.

This approach assumes that you can split up a large LCS task into a combination of smaller LCS tasks. Let's look at the short example in more detail:

    * A = 'ABCD'
    * B = 'BD'

We can see right away that the longest subsequence of letters here is 2 (B and D are in sequence in both strings). And we can calculate this by looking at relationships between each letter in the two strings, A and B.

Here, I have a matrix with the letters of A on top and the letters of B on the left side:


![Longest Common Subsequence](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Graph%20Algorithms/graph.PNG "Longest Common Subsequence")




This starts out as a matrix that has as many columns and rows as letters in the strings S and O +1 additional row and column, filled with zeros on the top and left sides. So, in this case, instead of a 2x4 matrix it is a 3x5.

Now, we can fill this matrix up by breaking it into smaller LCS problems. For example, let's first look at the shortest substrings: the starting letter of A and B. We'll first ask, what is the Longest Common Subsequence between these two letters "A" and "B"?

Here, the answer is zero and we fill in the corresponding grid cell with that value.


