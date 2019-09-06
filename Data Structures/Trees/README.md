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



