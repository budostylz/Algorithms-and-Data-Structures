# Algorithms-and-Data-Structures

## Python
https://docs.python.org/3/library/time.html

## Udacity Data Structures and Algorithms
https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256

## Online Psuedocode Editor
https://code2flow.com/app

## List of algorithms

https://en.wikipedia.org/wiki/List_of_algorithms

## Java™ Platform, Standard Edition 7 API Specification

https://docs.oracle.com/javase/7/docs/api/

## DOODLE

https://www.jdoodle.com/online-java-compiler

## Java - Basic Syntax

https://docs.oracle.com/javase/7/docs/api/

## Insertion Sort

https://www.geeksforgeeks.org/insertion-sort/

## Merge Sort

https://www.geeksforgeeks.org/merge-sort/

## Linear Search

https://www.geeksforgeeks.org/linear-search/

## Binary Search

https://www.geeksforgeeks.org/binary-search/

## Flowgorithm
http://www.flowgorithm.org/index.htm

## Sorting Algorithms
https://brilliant.org/wiki/sorting-algorithms/

## Python Program for QuickSort
https://www.geeksforgeeks.org/python-program-for-quicksort/

##------------------------------------------------------------------------------------------------------------------------------
# Arrays and Linked Lists

# Collections

## Why data structures?

Data structures are containers that organize and group data together in different ways. When you write code to solve a problem, there will always be data involved—and how you store or structure that data in the computer's memory can have a huge impact on what kinds of things you can do with it and how efficiently you can do those things.

In this section, we'll start out by reviewing some basic data structures that you're probably at least partly familiar with already.

Then, as we go on in the course, we'll consider the pros and cons of using different structures when solving different types of problems.

We'll start with a discussion of a very general structure—a collection.

https://youtu.be/cZORvZq-tI0

## Properties of collections

As Brynn discussed, collections:

    * Don't have a particular order (so you can't say "give me the 3rd element in this collection")
    * Don't have to have objects of the same type

# Lists
https://youtu.be/KUQSgUMtyv0

## Properties of lists

As Brynn described, lists:

    Have an order (so you can say things like "give me the 3rd item in the list")
    Have no fixed length (you can add or remove elements)

## Linked Lists Introduction
https://youtu.be/zxkpZrozDUk

## Linked Lists Continued
https://youtu.be/ZONGA5wmREI

Types of Linked Lists

In this notebook we'll explore three versions of linked-lists: singly-linked lists, doubly-linked lists, and circular lists.
Singly Linked Lists

In this linked list, each node in the list is connected only to the next node in the list.

Singly Linked List

This connection is typically implemented by setting the next attribute on a node object itself.

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
  
 # A small linked list:

head = Node(1)
head.next = Node(2)
        

```














