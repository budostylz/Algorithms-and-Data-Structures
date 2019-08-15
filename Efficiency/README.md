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
