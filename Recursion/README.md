# Recursion
We're going to take a break from our tour of data structures in order to look at the concept of recursion. Recursion is going to be a useful tool for solving some of the problems we'll be tackling later on, and this is a good place to introduce it and get some practice using it with the data structures we're reviewing.

When you hear the terms recursion or recursive, this might remind you of the terms repetition and repetitive—and this is a good connection, because recursion does indeed involve repetition. However, recursion isn't just about repetition.

With recursion, we solve a problem by first solving smaller instances of the same problem. In practice, this often involves calling a function from within itself—in other words, we feed some input into the function, and the function produces some output—which we then feed back into the same function. And we continue to do this until we arrive at the solution.

https://youtu.be/_aI2Jch6Epk

## Call stack
https://en.wikipedia.org/wiki/Call_stack

![Recursion](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/recursion.PNG "Recursion")

```python

def power_of_2(n):
    if n == 0:
        return 1
    
    return 2 * power_of_2(n - 1)

print(power_of_2(5))


```
![Recursion2](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/recursion2.PNG "Recursion2")

![Call Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Recursion/callstack.PNG "Call Stack")


```python

def sum_integers(n):
    if n == 1:
        return 1
    
    return n + sum_integers(n -1)

print(sum_integers(3))



```

## Gotchas
When using recursion, there are a few things to look out for that you don't have to worry about when running a loop (iteratively). Let's go over a few of those items.

## Call Stack
We went over an example of the call stack when calling power_of_2(5) above. In this section, we'll cover the limitations of recursion on a call stack. Run the cell below to create a really large stack. It should raise the error RecursionError: maximum recursion depth exceeded in comparison.

```python
print(power_of_2(10000))

```

Python has a limit on the depth of recursion to prevent a <a href="https://en.wikipedia.org/wiki/Stack_overflow">stack overflow</a>. However, some compilers will turn <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions">tail-recursive functions</a> into an iterative loop to prevent recursion from using up the stack. Since Python's compiler doesn't do this, you'll have to watch out for this limit.

## Slicing
Let's look at recursion on arrays and how you can run into the problem of slicing the array. If you haven't heard the term slicing, it's the operation of taking a subset of some data. For example, the list a can be sliced using the following operation: a[start:stop]. This will return a new list from index start (inclusive) to index stop (exclusive).

Let's look at an example of a recursive function that takes the sum of all numbers in an array. For example, the array of [5, 2, 9, 11] would sum to 27 (5 + 2 + 9 + 11).

```python
def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr))

```

Looking at this, you might think it has a running time of O( 𝑛 ), but that isn't correct due to the slice operation array[1:]. This operation will take O( 𝑘 ) time to run where  𝑘  is the number of elements to copy. So, this function is actually O( 𝑘∗𝑛 ) running time complexity and O( 𝑘∗𝑛 ) space complexity.

To visualize this, let's plot the time it takes to slice.

```python

import matplotlib.pyplot as plt
import statistics
import time
%matplotlib inline

n_steps = 10
step_size = 1000000
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
times = []

# Calculate the time it takes for the slice function to run with different sizes of k
for array_size in array_sizes:
    start_time = time.time()
    big_array[:array_size]
    times.append(time.time() - start_time)

# Graph the results
plt.scatter(x=array_sizes, y=times)
plt.ylim(top=max(times), bottom=min(times))
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()



```

