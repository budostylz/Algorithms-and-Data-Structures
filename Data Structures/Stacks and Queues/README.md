# Stacks and Queues

# Stack Details
https://youtu.be/HpaVHzDeZC4

![Stack](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Stacks%20and%20Queues/stack_walkthrough.PNG "Stack")

```python

#Stack Data Structure: Last In First Out(LIFO)

class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity...")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -=1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


foo = Stack()
#foo.push(1)
#foo.push(2)
#foo.push(3)
#foo.push(4)
#foo.push(5)
#foo.push(6)
#foo.push(7)
#foo.push(8)
#foo.push(9)
#foo.push(10) # The array is now at capacity!
#foo.push(11) # This one should cause the array to increase in size
#print(foo.arr) # Let's see what the array looks like now!
#print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.

#print(foo.size())
#print(foo.is_empty())

foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack

```

## Implement a stack using a linked list
Previously, we looked at how to implement a stack using an array. While that approach does work, we saw that it raises some concerns with time complexity. For example, if we exceed the capacity of the array, we have to go through the laborious process of creating a new array and moving over all the elements from the old array.

What if we instead implement the stack using a linked list? Can this improve our time complexity? Let's give it a try.

## 1. Define a Node class
Since we'll be implementing a linked list for this, we know that we'll need a Node class like we used earlier in this lesson.

## 2. Create the Stack class and its __init__ method
In the cell below, see if you can write the __init__ method for our Stack class. It will need two attributes:

* A head attribute to keep track of the first node in the linked list
* A num_elements attribute to keep track of how many items are in the stack

## 3. Add the push method
Next, we need to define our push method, so that we have a way of adding elements to the top of the stack.

## 4. Add the size and is_empty methods
When we implemented a stack using an array, we had these same methods. They'll work exactly the same way here—they aren't affected by the use of a linked list versus an array.

* Add a size method that returns the current size of the stack
* Add an is_empty method that returns True if the stack is empty and False otherwise

## 5. Add the pop method
The last thing we need to do is add the pop method. First, here's a walkthrough that describes how the method works:

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")

```

## Time complexity of stacks using linked lists
Notice that if we pop or push an element with this stack, there's no traversal. We simply add or remove the item from the head of the linked list, and update the  head reference. So with our linked list implementaion, pop and push have a time complexity of O(1).

Also notice that using a linked list avoids the issue we ran into when we implemented our stack using an array. In that case, adding an item to the stack was fine—until we ran out of space. Then we would have to create an entirely new (larger) array and copy over all of the references from the old array.

That happened because, with an array, we had to specify some initial size (in other words, we had to set aside a contiguous block of memory in advance). But with a linked list, the nodes do not need to be contiguous. They can be scattered in different locations of memory, an that works just fine. This means that with a linked list, we can simply append as many nodes as we like. Using that as the underlying data structure for our stack means that we never run out of capacity, so pushing and popping items will always have a time complexity of O(1).


## Building a Stack in Python
Before we start let us reiterate they key components of a stack. A stack is a data structure that consists of two main operations: push and pop. A push is when you add an element to the top of the stack and a pop is when you remove an element from the top of the stack. Python 3.x conviently allows us to demonstate this functionality with a list. When you have a list such as [2,4,5,6] you can decide which end of the list is the bottom and the top of the stack respectivley. Once you decide that, you can use the append, pop or insert function to simulate a stack. We will choose the first element to be the bottom of our stack and therefore be using the append and pop functions to simulate it. Give it a try by implementing the function below!

```python

# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")

```

## Balanced Parentheses Exercise
In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as: ((32+8)∗(5/2))/(2+6). In real life you can see this extend to many things such as text editor plugins and interactive development environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.

Try to code up a solution and pass the test cases.

```python

# Solution

# Our Stack Class
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() == None:
                return False

    if stack.size() == 0:
        return True
    else:
        return False


print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")

```

## Reverse Polish Notation
Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.

When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands. For example: 5 + 7 - 3 * 8

However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *

The above expression would be evaluated as (3 + 1) * 4 = 16

The goal of this exercise is to create a function that does the following:

Given a postfix expression as input, evaluate and return the correct final answer.
Note: In Python 3, the division operator / is used to perform float division. So for this problem, you should use int() after every division to convert the answer to an integer.

```python

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)


```

## Problem Statement
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).

```python

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def reverse_stack(stack):
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)


def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)

def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)
    
    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)

```

## Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.

```python

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            top = stack.top()
            if top != bracket:
                if top == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    ls = list()
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]          
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_1)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_3)


```

# Queues
https://youtu.be/XAbzlilAHZw

![Queue](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Stacks%20and%20Queues/queues.PNG "Queue")

## 1. Create the queue class and its __init__ method

## 2. Add the enqueue method

## 3. Add the size,  is_empty, and front methods
Just like with stacks, we need methods to keep track of the size of the queue and whether it is empty. We can also add a front method that returns the value of the front element.

* Add a size method that returns the current size of the queue
* Add an is_empty method that returns True if the queue is empty and False otherwise
* Add a front method that returns the value for the front element (whatever item is located at the front_index position). If the queue is empty, the front method should return None.

## 4. Add the dequeue method

## 5. Add the _handle_queue_capacity_full method

First, define the _handle_queue_capacity_full method:

* Define an old_arr variable and assign the the current (full) array so that we have a copy of it
* Create a new (larger) array and assign it to arr.
* Iterate over the values in the old array and copy them to the new array. Remember that you'll need two for loops for this.
Then, in the enqueue method:

* Add a conditional to check if the queue is full; if it is, call  _handle_queue_capacity_full

```python

class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # if queue is already full --> increase capacity
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")


```

![Queue & Linked List](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Stacks%20and%20Queues/queue_linked_list.PNG "Queue & Linked List")

## 1. Define a Node class

## 2. Create the Queue class and its __init__ method
In the cell below, see if you can write the __init_ method for our Queue class. It will need three attributes:

* A head attribute to keep track of the first node in the linked list
* A tail attribute to keep track of the last node in the linked list
* A num_elements attribute to keep track of how many items are in the stack

## 3. Add the enqueue method
In the cell below, see if you can figure out how to write the enqueue method.

Remember, the purpose of this method is to add a new item to the back of the queue. Since we're using a linked list, this is equivalent to creating a new node and adding it to the tail of the list.

Some things to keep in mind:

* If the queue is empty, then both the head and tail should refer to the new node (because when there's only one node, this node is both the head and the tail)
* Otherwise (if the queue has items), add the new node to the tail (i.e., to the end of the queue)
* Be sure to shift the tail reference so that it refers to the new node (because it is the new tail)

## 4. Add the size and is_empty methods
You've implemented these a couple of times now, and they'll work the same way here:

* Add a size method that returns the current size of the stack
* Add an is_empty method that returns True if the stack is empty and False otherwise

We'll make use of these methods in a moment when we write the dequeue method.

## 5. Add the dequeue method
In the cell below, see if you can add the deqeueue method.

Here's what it should do:

* If the queue is empty, it should simply return None. Otherwise...
* Get the value from the front of the queue (i.e., the head of the linked list)
* Shift the head over so that it refers to the next node
* Update the num_elements attribute
* Return the value that was dequeued

```python

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
        
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")

```
## Time Complexity
So what's the time complexity of adding or removing things from our queue here?

Well, when we use enqueue, we simply create a new node and add it to the tail of the list. And when we dequeue an item, we simply get the value from the head of the list and then shift the head variable so that it refers to the next node over.

Both of these operations happen in constant time—that is, they have a time-complexity of O(1).

## Build a Queue From Stacks
In this exercise we are going to create a queue with just stacks.

```python

# Solution 

# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.instorage=Stack()
        self.outstorage=Stack()
        
    def size(self):
         return self.outstorage.size() + self.instorage.size()
        
    def enqueue(self,item):
        self.instorage.push(item)
        
    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()
    
        
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail") 

```

```python

# Solution 

class Queue:
    def __init__(self):
         self.storage = []
    
    def size(self):
         return len(self.storage)
    
    def enqueue(self, item):
         self.storage.append(item)

    def dequeue(self):
         return self.storage.pop(0)

        
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")

```

## Reversed Queue
Write a function that takes a queue as an input and returns a reversed version of it.

```python

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


        
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")

def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1) 

test_case_2 = [1]
test_function(test_case_2)



```