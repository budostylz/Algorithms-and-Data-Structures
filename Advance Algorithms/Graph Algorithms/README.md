# Greedy Algorithms

## Introduction
Greedy algorithms is the collective name given to algorithms which make use of the Greedy Technique. The step by step process of these algorithms may be different. However, if any algorithm follows the Greedy Technique at each step, it can be called as a Greedy Algorithm.

Let's talk more about this greedy technique.

As the name suggests, in greedy technique, we get greedy and follow the best possible solution at each step of the algorithm.

Consider the following scenario

The following 4 points - A, B, C, D denote 4 corners of a city. You are standing at A and want to reach D as soon as possible. . However, there are only two ways in which you can do this. You can either go via B or you can go via C.

* Reaching B from A takes 1 min and reaching D from B takes 10 mins.
* Reaching C from A takes 5 min and reaching D from C takes 10 mins.

![Greedy](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Greedy%20Algorithms/greedy1.PNG "Greedy")

If we follow the greedy technique, we will choose to go via B. If we go to C, it would take 5 mins. However, going to B only takes 1 min. Therefore, while standing at A, going via B seems to be the better solution.

Thus, in our final solution, we will reach D in 11 minutes if we follow the greedy technique.

Let's consider the same scenario again but with slight changes.

This time, let the time taken to reach D from B be 20 minutes.

![Greedy](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Greedy%20Algorithms/greedy2.PNG "Greedy")

If we follow the greedy technique again, we will have to go via B because when we are at A going to B seems like a better choice.

But notice that if we go via B, the total time taken to reach D will be 21 minutes compared to 15 minutes if we go via C. So in this case following the greedy approach does not help us. Rather, it gives us a less efficient solution.

This is a key point to remember. Greedy Algorithms might not be the most effective at all times. Rather, in most of the cases, greedy solutions tend to have worse efficiency compared to some of the other techniques such as Divide and Conquer, Dynamic Programming etc. However, there are problems where following the greedy approach also results in an efficient - best overall solution.

Some of the famous greedy algorithms ares:

1. Dijkstra's Shortest Path Algorithm
2. A* search Algorithm
3. Prim's algorithm for Minimal Spanning Tree
4. Kruskal's algorithm for Minimal Spanning Tree
5. Knapsack Problem
6. Travelling Salesman Problem

## Takeaways
1. In a greedy solution, we go for the best possible choice at each step of the algorithm.

2. Because we are not considering future scenarios (and are only concerned with the best choice at each step), a greedy solution might not be the most effective solution for the problem.

To decide whether or not to use a greedy approach for a particular problem, try to think whether or not the greedy technique will work for all the future steps of the algorithm.

## Min Platforms Excercise

## Problem Statement
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345

```python

def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    platform_count = 1
    output = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):

        if arrival[i] < departure[j]:
            platform_count += 1
            i += 1

            if platform_count > output:
                output = platform_count
        else:
            platform_count -= 1
            j += 1

    return output

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]
test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)

```

## Min Operations

Starting from the number 0, find the minimum number of operations required to reach a given positive target number. You can only use the following two operations:

1. Add 1
2. Double the number

## Example:
1. For Target = 18, output = 6, because it takes at least 6 steps shown below to reach the target

* start = 0
* step 1 ==> 0 + 1 = 1
* step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
* step 3 ==> 2 * 2 = 4
* step 4 ==> 4 * 2 = 8
* step 5 ==> 8 + 1 = 9
* step 6 ==> 9 * 2 = 18

2. For Target = 69, output = 9, because it takes at least 8 steps to reach 69 from 0 using the allowed operations

* start = 0
* step 1 ==> 0 + 1 = 1
* step 2 ==> 1 + 1 = 2
* step 3 ==> 2 * 2 = 4
* step 4 ==> 4 * 2 = 8
* step 5 ==> 8 * 2 = 16
* step 6 ==> 16 + 1 = 17
* step 7 ==> 17 * 2 = 34
* step 8 ==> 34 * 2 = 68
* step 9 ==> 68 + 1  = 69


```python

def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0
    
    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        num_steps += 1
    return num_steps


# Test Cases

def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)

target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)





```



