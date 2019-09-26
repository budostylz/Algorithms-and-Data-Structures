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

## Complexity

What was the complexity of this?

In the solution, we are looping over the elements of our input_string using two for loops; these are each of 𝑂(𝑁)
and nested this becomes 𝑂(𝑁^2). This behavior dominates our optimized solution.

## Coin Change

You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

As an example:

    Input: coins = [1, 2, 3], amount = 6
    Output: 2
    Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use 3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.

There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.


```python

'''

# Solution One

# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

# Base Cases: 
    # when Amount == 0: F(Amount) = 0
    # when Amount < 0: F(Amount) =  float('inf')

def coin_change(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}
    
    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0 
        
        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]
    
    res = return_change(amount)
    
    # return -1 when no change found
    return -1 if res == float('inf') else res


'''

# Solution Two

# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')]*(amount + 1)
    
    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0
    
    i = 0
    while (i < amount):
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i+coin] = min(res[i] + 1, res[i+coin])
        i += 1

    if res[amount] == float('inf'):
        return -1
    return res[amount]
        



def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)





```

## Stock Prices

You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

prices = [3, 4, 7, 8, 6]

* Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.

In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.

Fill out the function below and run it against the test cases. Take into consideration the time complexity of your solution.


```python

# Solution

def max_returns(arr):
    """
    The idea is to pick two dates:
        1. buy date
        2. sell date
    We will keep track of our max profit while iterating over the list
    At each step we will make the greedy choice by choosing prices such that our profit is maximum 
    """
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    
    if len(arr) < 2:
        return
    
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit

# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)





```



