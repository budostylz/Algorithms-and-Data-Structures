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

