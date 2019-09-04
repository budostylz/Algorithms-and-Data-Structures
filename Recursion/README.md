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

