# Efficiency
We said earlier that this Nanodegree program is about how to write code to solve problems and to do so efficiently.

In the last section, we looked at some basic aspects of solving problems—but we didn't really think too much about whether our solutions were efficient.

## Space and time
When we refer to the efficiency of a program, we aren't just thinking about its speed—we're considering both the time it will take to run the program and the amount of space the program will require in the computer's memory. Often there will be a trade-off between the two, where you can design a program that runs faster by selecting a data structure that takes up more space—or vice versa.

https://video.udacity-data.com/topher/2016/September/57d116e4_efficiency/efficiency_720p.mp4

Algorithms
        An algorithm is essentially a series of steps for solving a problem. Usually, an algorithm takes some kind of input (such as an unsorted list) and then produces the desired output (such as a sorted list).

For any given problem, there are usually many different algorithms that will get you to exactly the same end result. But some will be much more efficient than others. To be an effective problem solver, you'll need to develop the ability to look at a problem and identify different algorithms that could be used—and then contrast those algorithms to consider which will be more or less efficient.

## But computers are so fast!
Sometimes it seems like computers run programs so quickly that efficiency shouldn't really matter. And in some cases, this is true—one version of a program may take 10 times longer than another, but they both still run so quickly that it has no real impact.

But in other cases, a small difference in how your code is written—or a tiny change in the type of data structure you use—can mean the difference between a program that runs in a fraction of a millisecond and a program that takes hours (or even years!) to run.

## Quantifying efficiency
It's fine to say "this algorithm is more efficient than that algorithm", but can we be more specific than that? Can we quantify things and say how much more efficient the algorithm is?

Let's look at a simple example, so that we have something specific to consider.

Although the two functions have the exact same end result, one of them iterates many times to get to that result, while the other iterates only a couple of times.

This was admittedly a rather impractical example (you could skip the for loop altogether and just add 200 to the input), but it nevertheless demonstrates one way in which efficiency can come up.

## Counting lines
With the above examples, what we basically did was count the number of lines of code that were executed. Let's look again at the first function:

```python

def some_function(n):
    for i in range(2):
        n += 100
    return n

```

There are four lines in total, but the line inside the for loop will get run twice. So running this code will involve running 5 lines.

Now let's look at the second example:

```python

def other_function(n):
    for i in range(100):
        n += 2
    return n

```
In this case, the code inside the loop runs 100 times. So running this code will involve running 103 lines!

Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we go through the program. But in this case, it's an easy way for us to approximate the difference in efficiency between the two solutions. We can see that if Python has to perform an addition operation 100 times, this will certainly take longer than if it only has to perform an addition operation twice!



![Comparison, Computational, Complexity](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Efficiency/comparison_computational_complexity.PNG "Comparison, Computational, Complexity")
<a href="https://commons.wikimedia.org/wiki/File:Comparison_computational_complexity.svg">"Comparison of computational complexity" by Cmglee. Used under CC BY-SA 4.0.</a>

## Quadratic Example
```python

# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print ("Items: {}, {}".format(first_loop_item,second_loop_item))
            
            
Quad_Example([1,2,3,4])

%time

"""
Items: 1, 1
Items: 1, 2
Items: 1, 3
Items: 1, 4
Items: 2, 1
Items: 2, 2
Items: 2, 3
Items: 2, 4
Items: 3, 1
Items: 3, 2
Items: 3, 3
Items: 3, 4
Items: 4, 1
Items: 4, 2
Items: 4, 3
Items: 4, 4
CPU times: user 3 µs, sys: 1 µs, total: 4 µs
Wall time: 6.68 µs
"""

```

##Log Linear Example

```python

# O(nlogn)

# Don't worry about how this algorithm works, we will cover it later in the course!

def Log_Linear_Example(our_list):
    
    if len(our_list) < 2:
        return our_list
    
    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k]=left[i]
                i+=1
            else:
                our_list[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            our_list[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            our_list[k]=right[j]
            j+=1
            k+=1
        
        return our_list

Log_Linear_Example([56,23,11,90,65,4,35,65,84,12,4,0])

%time
"""
CPU times: user 2 µs, sys: 1 µs, total: 3 µs
Wall time: 6.2 µs
"""
```

## Linear Example
```python

# O(n)

def Linear_Example(our_list):
    for item in our_list:
        print ("Item: {}".format(item))

Linear_Example([1,2,3,4])
%time

"""
Item: 1
Item: 2
Item: 3
Item: 4
CPU times: user 3 µs, sys: 0 ns, total: 3 µs
Wall time: 6.68 µs

"""



```

## Logarithmic Example

```python

# O(logn)

def Logarithmic_Example(number):
    if number == 0: 
        return 0
    
    elif number == 1: 
        return 1
    
    else: 
        return Logarithmic_Example(number-1)+Logarithmic_Example(number-2)

    
Logarithmic_Example(29)

%time

"""
CPU times: user 3 µs, sys: 0 ns, total: 3 µs
Wall time: 7.63 µs

"""
```

## Constant Example

```python

# O(1)

def Constant_Example(our_list):
    return our_list.pop()

Constant_Example([1,2,3,4])

%time

"""
CPU times: user 3 µs, sys: 0 ns, total: 3 µs
Wall time: 8.58 µs

"""

```
