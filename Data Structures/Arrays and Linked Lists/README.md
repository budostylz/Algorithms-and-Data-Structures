# Collections

## Why data structures?
Data structures are containers that organize and group data together in different ways. When you write code to solve a problem, there will always be data involved—and how you store or structure that data in the computer's memory can have a huge impact on what kinds of things you can do with it and how efficiently you can do those things.

In this section, we'll start out by reviewing some basic data structures that you're probably at least partly familiar with already.

Then, as we go on in the course, we'll consider the pros and cons of using different structures when solving different types of problems.

We'll start with a discussion of a very general structure—a collection.

# Collections
https://youtu.be/cZORvZq-tI0

## Properties of collections
As Brynn discussed, collections:

 * Don't have a particular order (so you can't say "give me the 3rd element in this collection")
 * Don't have to have objects of the same type

 # Lists
 https://youtu.be/KUQSgUMtyv0

 ## Properties of lists
As Brynn described, lists:

* Have an order (so you can say things like "give me the 3rd item in the list")
* Have no fixed length (you can add or remove elements)

# Arrays

https://youtu.be/OnPP5xDmFv0

## Arrays vs. lists vs. Python lists
The distinction between arrays and lists can be a little confusing, especially because of how Python implements the data structure it calls a "list". Below, we'll go over some key points that should make this clearer.

## Arrays
An array has some things in common with a list. In both cases:

* There is a collection of items
* The items have an order to them

But as Brynn discussed in the video, one of the key differences is that arrays have indexes, while lists do not.

To understand this, it helps to know how arrays are stored in memory. When an array is created, it is always given some initial size—that is, the number of elements it should be able to hold (and how large each element is). The computer then finds a block of memory and sets aside the space for the array.

Importantly, the space that gets set aside is one, continuous block. That is, all of the elements of the array are contiguous, meaning that they are all next to one another in memory.

Another key characteristic of an array is that all of the elements are the same size.

When we represent an array visually, we often draw it as a series of boxes that are all of the same size and all right next to one another:

![Array](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/arr1.PNG "Array")

Because all of the elements are 1) next to one another and 2) the same size, this means that if we know the location of the first element, we can calculate the location of any other element.

For example, if the first element in the array is at memory location 00 and the elements are 24 bytes, then the next element would be at location 00 + 24 = 24. And the one after that would be at 24 + 24 = 48, and so on.

Since we can easily calculate the location of any item in the array, we can assign each item an index and use that index to quickly and directly access the item.

![Array](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/arr2.PNG "Array")

## Lists
In contrast, the elements of a list may or may not be next to one another in memory! For example, later in this lesson we'll look at linked lists, where each list item points to the next list item—but where the items themselves may be scattered in different locations of memory. In this case, knowing the location of the first item in the list does not mean you can simply calculate the location of the other items. This means we cannot use indexes to directly access the list items as we would in an array. We'll explore linked lists in more detail shortly.

## Python lists
In Python, we can create a list using square brackets [ ]. For example:

```python

my_list = ['a', 'b', 'c']
my_list
['a', 'b', 'c']


```

```python

 my_list[0]
'a'
 my_list[1]
'b'
 my_list[2]
'c'


```
But wait, didn't we just say that lists don't have indexes!? This seems to directly contradict that distinction.

The reason for this confusion is simply one of terminology. The earlier description we gave of lists is correct in general—that is, usually when you hear someone refer to something as a "list", that is what they mean. However, in Python the term is used differently.

We will not get into all of the details, but the important thing you need to know for this course is the following: If you were to look under the hood, you would find that a Python list is essentially implemented like an array (specifically, it behaves like a dynamic array, if you're curious). In particular, the elements of a Python list are contiguous in memory, and they can be accessed using an index.

In addition to the underlying array, a Python list also includes some additional behavior. For example, you can use things like pop and append methods on a Python list to add or remove items. Using those methods, you can essentially utilize a Python list like a stack (which is another type of data structure we'll discuss shortly).

In general, we will try to avoid using things like pop and append, because these are high-level language features that may not be available to you in other languages. In most cases, we will ignore the extra functionality that comes with Python lists, and instead use them as if they were simple arrays. This will allow you to see how the underlying data structures work, regardless of the language you are using to implement those structures.

Here's the bottom line:

* Python lists are essentially arrays, but also include additional high-level functionality
* During this course, we will generally ignore this high-level functionality and treat Python lists as if they were simple arrays

This approach will allow you to develop a better understanding for the underlying data structures.

# Linked Lists
https://youtu.be/zxkpZrozDUk

https://youtu.be/ZONGA5wmREI

![Singly](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/singly_linked_list.PNG "Singly")


```python

# Singly Linked List Data Structure
# 2(Head) -> 1 -> 4 -> 3 -> 5 -> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

#print(head.value)
#print(head.next.value)
#print(head.next.next.value)
#print(head.next.next.next.value)
#print(head.next.next.next.next.value)


def print_linked_list(head):
    current_node = head
    
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
        
print_linked_list(head)


```
Above we have a simple linked list with two elements, [1, 2]. Usually you'll want to create a LinkedList class as a wrapper for the nodes themselves and to provide common methods that operate on the list. For example you can implement an append method that adds a value to the end of the list. Note that if we're only tracking the head of the list, this runs in linear time -  <strong>𝑂(𝑁)</strong>  - since you have to iterate through the entire list to get to the tail node. However, prepending (adding to the head of the list) can be done in constant  <strong>𝑂(1)</strong>  time. You'll implement this prepend method in the Linked List Practice notebook.

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")



```
![Doubly](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/doubly_linked_list.PNG "Doubly")

```python
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Solution
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
            
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

# Test your class here

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous

```

![Circular](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/circular_linked_list.PNG "Circular")

A circular linked list is typically considered pathological because when you try to iterate through it, you'll never find the end. We usually want to detect if there is a loop in our linked lists to avoid these problems. You'll get a chance to implement a solution for detecting loops later in the lesson.

# Linked List Practice
Implement a linked list class. Your class should be able to:

* Append data to the tail of the list and prepend to the head
* Search the linked list for a value and return the node
* Remove a node
* Pop, which means to return the first node's value and delete the node from the list
* Insert data at some position in the list
* Return the size (length) of the linked list

```python

# Solution

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value)
            return

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def append(self, value):
        """ Append a node to the end of the list """
        # Here I'm not keeping track of the tail. It's possible to store the tail
        # as well as the head, which makes appending like this an O(1) operation.
        # Otherwise, it's an O(N) operation as you have to iterate through the
        # entire list to add a new tail.

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")


    def remove(self, value):
        """ Delete the first node with the desired data. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")


    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

print(linked_list)


```

# Reversing a linked list exercise
Given a singly linked list, return another linked list that is the reverse of the first.

```python

# Solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

# Time complexity O(N)
def reverse(linked_list):
       
    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to 
    # the new linked list
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
    new_list.head = prev_node
    return new_list

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")

```

![Loop](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/loops.PNG "Loop")


```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next 
node.next = loop_start

# Solution

def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
    # the list has an end and isn't circular
    return False

small_loop = LinkedList([0])
small_loop.head.next = small_loop.head
print ("Pass" if iscircular(list_with_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print ("Pass" if not iscircular(LinkedList([1])) else "Fail")
print ("Pass" if iscircular(small_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([])) else "Fail")

```

## Flattening a nested linked list
Suppose you have a linked list where the value of each node is a sorted linked list (i.e., it is a nested list). Your task is to flatten this nested list—that is, to combine all nested lists into a single (sorted) linked list.

```python

# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    #print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next


```

![Computational Complexity](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/computational_complexity.PNG "Computational Complexity")

![Add One](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/add1.PNG "Add One")

```python

# Solution
def add_one(arr):
    output = 1;

    for i in range(len(arr), 0, -1):
        output = output + arr[i - 1]
        borrow = output//10
        if borrow == 0:
            arr[i - 1] = output
            break
        else:
            arr[i - 1] = output % 10
            output = borrow
    arr = [borrow] + arr
    index = 0
    while arr[index]==0:
        index += 1
    return arr[index:]

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass") 
    
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)


```

![Duplicate Number](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/duplicate_number.PNG "Duplicate Number")

```python

# Solution
def add_one(arr):
    output = 1;

    for i in range(len(arr), 0, -1):
        output = output + arr[i - 1]
        borrow = output//10
        if borrow == 0:
            arr[i - 1] = output
            break
        else:
            arr[i - 1] = output % 10
            output = borrow
    arr = [borrow] + arr
    index = 0
    while arr[index]==0:
        index += 1
    return arr[index:]

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass") 
    
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)




```
![Max Sum](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/maxSum.PNG "Max Sum")

```python

# Solution
def max_sum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements
test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
test_case = [arr, solution]
test_function(test_case)



```

## Pascal's Triangle
https://www.mathsisfun.com/pascals-triangle.html

![Pascal's Triangle](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/pascalsTriangle.PNG "Pascal's Triangle")

```python

# Solution

def nth_row_pascal(n):
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

n = 0
solution = [1]
test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]
test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]
test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]
test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]
test_case = [n, solution]
test_function(test_case)

```

![Even Odd](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/even_odd.PNG "Even Odd")

```python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution
def even_after_odd(head):
    
    if head is None:
        return head
    
    even = None
    odd = None
    even_tail = None
    head_tail = None
    
    while head:
        next_node = head.next
        
        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if odd is None:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        head.next = None
        head = next_node
    
    if odd is None:
        return even
    odd_tail.next = even
    return odd

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

```

![Skip i Remove j](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/skipi_removej.PNG "Skip i Remove j")

```python

# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Solution
def skip_i_delete_j(head, i, j):
    if i == 0:
        return None
    
    if head is None or j < 0 or i < 0:
        return head
    
    current = head
    previous = None
    while current:
        # skip (i - 1) nodes
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        # delete next j nodes
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        previous.next = current
    return head

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)

```

![Linked List Swap](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Arrays%20and%20Linked%20Lists/linked_list_swap.PNG "Linked List Swap")

```python

# Solution

class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, left_index, right_index):

    # if both the indices are same
    if left_index == right_index:
        return head
    
    
    left_previous = None
    left_current = None

    right_previous = None
    right_current = None

    count = 0
    temp = head
    new_head = None

    # find out previous and current node at both the indices
    while temp is not None:
        if count == left_index:
            left_current = temp
        elif count == right_index:
            right_current = temp
            break

        if left_current is None:
            left_previous = temp
        right_previous = temp
        temp = temp.next
        count += 1

    right_previous.next = left_current
    temp = left_current.next
    left_current.next = right_current.next

    # if both the indices are next to each other
    if left_index != right_index:
        right_current.next = temp

    # if the node at first index is head of the original linked list
    if left_previous is None:
        new_head = right_current
    else:
        left_previous.next = right_current
        new_head = head

    return new_head

def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2 
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)




```


