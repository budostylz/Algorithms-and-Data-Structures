# Graph Algorithms

https://youtu.be/DFR8F2Q9lgo

## What is a Graph
https://youtu.be/p-_DFOyEMV8

## DIrections and Cycles
https://youtu.be/lF0vUktQDPo

## Connectivity
https://youtu.be/4x6u2KtNDg4

## Edge List
https://youtu.be/uw9u6dtl0WA

## Adjacency Matricies
https://youtu.be/FsFhoTALA1c

## Graph Traversal
https://youtu.be/Dkt-XxHZaZE

## DFS
https://youtu.be/BC8jEidd2EQ

## BFS
https://youtu.be/pol4kGNlvJA

## Shortest Path 
https://youtu.be/huKUM97Vve8

## Diijkstra's Algorithm
https://youtu.be/SoPMK03cOgk

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#/media/File:Dijkstra_Animation.gif

## Diijkstra's Algorithm Step by Step
https://youtu.be/4xROtuo1xAw

## Graph Depth First Search
In this exercise, you'll see how to do a depth first search on a graph. To start, let's create a graph class in Python.


```python

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)



```

Now let's create the graph.

```python

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)



```

## Implement DFS

Using what you know about DFS for trees, apply this to graphs. Implement the dfs_search to return the GraphNode with the value search_value starting at the root_node.


```python

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]
    
    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                stack.append(child)

assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')





```

![Graph Algorithms](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Advance%20Algorithms/Graph%20Algorithms/graph.PNG "Graph Algorithms")

## Graph Depth-First Search With Recursion
We've done depth-first search previously using an iterative approach (i.e., using a loop). In this notebook, we'll show how to implement a recursive soluton.

The basic idea is to select a node and explore all the possible paths from that node, and to apply this recursively to each node we are exploring.

You can see some helpful illustrations with various combinations here: 

https://www.cs.usfca.edu/~galles/visualization/DFS.html

