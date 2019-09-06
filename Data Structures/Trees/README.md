# Trees 
https://youtu.be/oaxLPzaXRDc

https://youtu.be/mPUsDUR_sj8

## Tree Traversal
https://youtu.be/KZOdmzypynw

## Depth-First Traversal
https://youtu.be/wp5ohHFTieM

## Search and Delete
https://youtu.be/KbL-HK3ztX8

## Insert
https://youtu.be/FNxgFlPv8gA

## Binary Search Trees(BSTs)
https://youtu.be/7-ZQrugO-Yc

https://youtu.be/abRNGLhGUmE

## BST Complications
https://youtu.be/pcB0wV7myy4

## Practice Overview
https://youtu.be/J_fJHvf29b4

## Traverse a tree (depth first search)
Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.

Let's walk through pre-order traversal by hand first, and then try it out in code.

## Create a Binary Tree

![Binary Tree](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/binarytree.PNG "Binary Tree")


```python

## Define a node
class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left != None
         
    def has_right_child(self):
        return self.right != None
          

## Define a Tree
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root


node0 = Node("apple")
node1 = Node("banana")
node2 = Node("cherry")

print(f" has left child ? {node0.has_left_child()}")
print(f" has right child ? {node0.has_right_child()}")

print(" adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f" has left child ? {node0.has_left_child()}")
print(f" has right child ? {node0.has_right_child()}")


```

https://youtu.be/cixp2hq9_9w

https://youtu.be/9maTu-nA4Ec

https://youtu.be/UVYwV-z8bfk

https://youtu.be/ctNTo-pkF7g

https://youtu.be/IQy-bD-Cshw

https://youtu.be/O1U-QfGnQ3U

https://youtu.be/3wEcBGLM_Zo

https://youtu.be/VoGdhGqSO00

https://youtu.be/2Sf3ziM0K5Y

https://youtu.be/HsSIPEyXydQ

https://youtu.be/DxeYBbT_b8c

https://youtu.be/-YGl9VvFGDg

https://youtu.be/AC19_mrfKP4

## Code: DFS
https://youtu.be/SICCSQzv-qI

## Tree Setup
https://youtu.be/mopUeLXUKuY

## DFS uses a Stack
https://youtu.be/tKF60f2_tvs

## Coding Step by Step
https://youtu.be/ayuX5T-F-Hc

## DFS implementation with a Bug
Let's look at a common error, an infinite loop, and explain why this is happening.

https://youtu.be/oeEhpPGYRw8

## Tracking Additional Information in the Stack
https://youtu.be/P1XDtgILODk

## Code that tracks the State in the Stack
https://youtu.be/E68EQTBTGJo

## Pre-Order DFS with Recursion Code Intro
https://youtu.be/RAidcReoxqs

## DFS Pre-Order with Recursion Solution
https://youtu.be/um10vCBP2FE

## In-Order and Post-Order Code Intro
https://youtu.be/dN_F1xK6qTE

## In-Order and Post-Order Solution
https://youtu.be/4ruolshjhq0



```python

# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))




visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order}
stack:
{stack}
 """)

# visit apple
visit_order.append(node.get_value())
print(f"""
visit_order {visit_order}
{stack}
 """)

# check if apple has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# visit banana
visit_order.append(node.get_value())
print(f"""
visit_order {visit_order}
{stack}
 """)

# check if banana has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child (banana)
# we'll visit banana and add it to the stack

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# visit dates
visit_order.append(node.get_value())
print(f"""
visit_order {visit_order}
{stack}
 """)


```

```python

# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    stack.push(node)
    node = stack.top()
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit): 
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
        """)
        count +=1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node)
            # using top() is redundant, but added for clarity
            node = stack.top() 
            visit_order.append(node.get_value())
            
        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None
        
        
    return visit_order


class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s

def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order


def pre_order(tree):
    visit_order = list()
    root = tree.get_root()
    

    def traverse(node):

        if node:
            # visit
            visit_order.append(node.get_value())

            # traverse left
            traverse(node.get_left_child())

            # traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order

def in_order(tree):
    visit_order = list()
    root = tree.get_root()
    

    def traverse(node):

        if node:
            # traverse left
            traverse(node.get_left_child())

            # visit
            visit_order.append(node.get_value())   
            
            # traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order

def post_order(tree):
    visit_order = list()
    root = tree.get_root()
    

    def traverse(node):

        if node:
            # traverse left
            traverse(node.get_left_child())

            # traverse right
            traverse(node.get_right_child())

            # visit
            visit_order.append(node.get_value())   
            
          

    traverse(root)

    return visit_order
# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# pre-order traversal
#print( pre_order(tree) )

# in-order traversal
#print( in_order(tree) )

# post-order traversal
print( post_order(tree) )

#pre_order_with_stack_buggy(tree)

# check pre-order traversal
#pre_order_with_stack(tree, debug_mode=True)


```

## Breadth First Search intro
https://youtu.be/pmynsdbRg1U


![BFS](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/bfs.PNG "BFS")

![BFS](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/bfs2.PNG "BFS")

## Tree Setup
https://youtu.be/NEoeKt1rOQY

## Queue for Breadth First Search
https://youtu.be/HVVW7LV1Fk8

## Code up a Queue
https://youtu.be/6EaJnaFTZNE

## BFS Implementation Code intro
https://youtu.be/rP_DScEHVk4

## BFS Code Implementation Solution
https://youtu.be/EeqmCsKPPRQ

## BFS (Optional, Bonus): Print a Tree using BFS
https://youtu.be/AHtR_ZwVE-s

## Print a Tree Solution
https://youtu.be/7Tncq27bwyM


```python

from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

# this code makes the tree that we'll traverse
class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    
    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

visit_order = list()
q = Queue()


# start at the root node and add it to the queue
node = tree.get_root()
q.enq(node)
print(q)

# dequeue the next node in the queue.
# "visit" that node
# also add its children to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)


# dequeue the next node (banana)
# visit it, and add its children (dates) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)

# dequeue the next node (cherry)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)

# dequeue the next node (dates)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)


```

```python
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

# this code makes the tree that we'll traverse
class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
           
    def get_root(self):
        return self.root


# BFS algorithm
def bfs(tree):
    # queue
    q = Queue()

    # visit_order
    visit_order = list()

    # start at root
    node = tree.get_root()

    # add root to queue
    q.enq(node)

    # while queue is not empty:
    while len(q) > 0:
        # dequeue the node
        node = q.deq()
        # visit that node
        visit_order.append(node)
        # add left child if exists
        if node.has_left_child():
            q.enq(node.get_left_child())
        # add right child if exists
        if node.has_right_child():
            q.enq(node.get_right_child())

    # return the visit order
    return visit_order

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print( bfs(tree) )

```

## Binary Search Tree Intro
https://youtu.be/C_2akqGHlsc

![BST](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/bst.PNG "BST")

## Tree Setup
https://youtu.be/gbGFK5REl6g

## Insertion
https://youtu.be/SX0ThwOx-gE

## Insertion Code Intro
https://youtu.be/omrmXwZ5IKQ

## Insertion Code Solution
https://youtu.be/HTwhOLuIUBg

## Search
https://youtu.be/-SWRLeI08xU

## Search Code Intro
https://youtu.be/V4T6qDj7c8s

## Search Code Solution
https://youtu.be/vMtQdLTmu-E

## Delete
https://youtu.be/fJlWvaqqeZg

```python

from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


# this code makes the tree that we'll traverse
class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return

        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node's value
                node.set_value(new_node.get_value())
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison ==1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping


    """
    define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self,value):
        
        if self.get_root() == None:
            self.set_root(value)
            return
        #otherwise, use recursion to insert the node
        self.insert_recursively(self.get_root(), Node(value))

    def insert_recursively(self,node,new_node):
        comparison = self.compare(node,new_node)
        if comparison == 0:
            # equal
            node.set_value(new_node.get_value())
        elif comparison == -1:
            # traverse left
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(),new_node)
            else:
                node.set_left_child(new_node)
        else: #comparison == 1
            # traverse right
            if node.has_right_child():
                self.insert_recursively(node.get_right_child, new_node)
            else:
                node.set_right_child(new_node)
        
    def search(self,value):
        node = self.get_root()
        s_node = Node(value)
        while(True):
            comparison = self.compare(node, s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)


tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}

""")


```

![Diameter of Binary Tree](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/diameter.PNG "Diameter of Binary Tree")

![Diameter of Binary Tree](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/diameter2.PNG "Diameter of Binary Tree")

```python

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        from queue import Queue

from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

    
    

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


# Solution
def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]
    
def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    if root is None:
        return 0, 0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = diameter_of_binary_tree(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
solution = 6
test_case = [arr, solution]
test_function(test_case)


```

![Root to Node](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Data%20Structures/Trees/root_to_node.PNG "Root to Node")



```python

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

    
 # Solution
def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))

def path_from_node_to_root(root, data):
    if root is None:
        return None

    elif root.data == data:
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer
    return None
  
def test_function(test_case):
    arr = test_case[0]
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node(root, data)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
data = 5
solution = [1, 2, 5]
test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
data = 5
solution = [1, 3, 5]
test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 11
solution = [1, 3, 4, 6, 10, 11]
test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 8
solution = [1, 3, 5,8]
test_case = [arr, data, solution]
test_function(test_case)


```




