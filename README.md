# agh-wzmw-graphs

Learn few algorithms from Graph Theory in a fun way, but I also want to make it flexible.


Hello world! Simple graph:

```py
from graphlib.graphs.simple_graph import SimpleGraph


nodes_num = 10

# create a simple graph
G = SimpleGraph()
for _ in range(nodes_num):
    G.add_node()

# creating a cycle
# The ordeer of nodes in SimpleGraph.connect_nodes(n1, n2) does NOT matter!
for i, n in enumerate(G.V):
    if i+1 < nodes_num:
        G.connect_nodes(n, G.V[i+1])
        continue
    # join last and first element
    G.connect_nodes(G.V[0], G.V[-1])

for e in G.E:
    print(str(e))

# making a deepcopy:
G1 = G.copy()

def presentation():
    print(f"""
This displays how many connections to a certain node does this node have:
    {n2._neighbours[n1] = }
    {n1._neighbours[n2] = }
This displays what edges is this node part of.
    {[str(e) for e in n1.edges] = }
    {[str(e) for e in n2.edges] = }
""")
    

# DO NOT MIX UP G1 and G
# those are separate copies and you will imidietly run in to bugs
e = G1.E[0]
n1, n2 = e.nodes
n1, n2 = G1.get_nodes(0, 1)

print(f"{n1.id=}, {n2.id=}")

presentation()
print("G1.remove_edge(e)")
G1.remove_edge(e)
presentation()

# will destroy the edge with all consequences that can be expected
#   n1 and n2 wont be neigbours. 

# usefull methods
# Graph:

if False:
    # this will not run, it is simply to show accesible methods
    # (it is in wrong order)
    graph = SimpleGraph()
    n1 = graph.add_node() # create a node, append it to graph and return it
    n2 = graph.add_node()
    graph.connect_nodes(n1, n2) # create an edge between two nodes

    graph.remove_node(n2) # remove node and its edges
    graph.disconnect_nodes(n1, n2) # remvoe edge between two nodes
    graph.remove_edge(n1.edges[0]) # remove edge

    n1, n2 = graph.get_nodes(0, 1) # return two nodes
    graph.copy() # create a deep copy


```
Console output:
```
0<=>1
1<=>2
2<=>3
3<=>4
4<=>5
5<=>6
6<=>7
7<=>8
8<=>9
0<=>9
n1.id=0, n2.id=1

This displays how many connections to a certain node does this node have:
    n2._neighbours[n1] = 1
    n1._neighbours[n2] = 1
This displays what edges is this node part of.
    [str(e) for e in n1.edges] = ['0<=>1', '0<=>9']
    [str(e) for e in n2.edges] = ['0<=>1', '1<=>2']

G1.remove_edge(e)

This displays how many connections to a certain node does this node have:
    n2._neighbours[n1] = 0
    n1._neighbours[n2] = 0
This displays what edges is this node part of.
    [str(e) for e in n1.edges] = ['0<=>9']
    [str(e) for e in n2.edges] = ['1<=>2']
```

## SimpleGraph, Multigraph, DirectedGraph, Node, DirectedEdge, SimpleEdge, Edge:
### Methods and fields.


This is not an example of working code
This is just a presentation of those methods, with explentaion of what they do, and their arguments

#### SimpleGraph - <pl: graf prosty> 
##### no multiple edges are allowed. Edge connects exactly two nodes - SimpleEdge.
```py
graph = SimpleGraph()

graph.E # list of edges of this graph
graph.V # list of vertecies of this graph


# When creating new edges and nodes they are created with and id, that starts at 0 for the first node and edge
# So in the below exaples I assume you have allready created 5 edges, 
# If I want the edge with id 4 it means the graph has 5 edges in total.
# And the graph has to have at least 4 nodes.
edges: list[SimpleEdge] = graph.get_edges(4, 2) # list of which elements are objects of class SimpleEdge.
nodes: list[Node] = graph.get_nodes(0, 1, 2, 3) # list of which elements are objects of class Node.

# Example usage
e4, e2 = graph.get_edges(4, 2)
# the method returns a list, but when the number of elements in the list mathes number of variables I want to assign them to they are unpacked and ussigned to them, much like with a tuple.

# Create one node, and return it.
n1: Node = graph.add_node()

# Create n nodes and return list of them
n2, n3 = graph.add_nodes(2)

# Create an edge between two nodes.
graph.connect_nodes(n1, n3)

# Find edge that connects these two nodes, and remove it.
graph.disconnect_nodes(n1, n2)

# Create a path connecting these nodes, in the specified order.
graph.create_path(n1, n2, n3)

# Just like above, but as argument takes id's of nodes.
graph.create_path_ids(0, 1, 2) 

# Remove edge - disconnect nodes that are connected with this edge.
graph.remove_edge(e)

# Disconnect this node from all edges it has, remove it from graph.V. Object is permanently deleted.
graph.remove_node(n)

# Create a deep copy of the object.
graph.deepcopy()
```

#### Multigraph - <pl: multigraf> 
##### It is different from SimpleGraph in only one way: when connecting two new nodes, it does not check if they are allready connected.

```py
mgraph = Multigraph()
mgraph.add_nodes(2)
n1, n2 = mgraph.get_nodes(0, 1)
mgraph.connect_nodes(n1, n2)
mgraph.connect_nodes(n1, n2) # This line would throw an error if we were working with a SimpleGraph, but it wont, beacuse Multigraph allows multiple edges between two same nodes.
```


#### Node - <pl: wierzchołek>

```py
#  ~~~~~~ BAD ~~~~~~~~~
# One does NOT create a node in this way!!!!
n = Node()
# DO NOT DO THIS.

#  ~~~~~~ GOOD ~~~~~~~~~
# You create a node by first creating a graph, and only then do you use an appropriate method on this graph to create a Node associated with this graph.
graph = SimpleGraph()
n = graph.add_node()  # This is the proper way.
n1 = graph.add_node() # graph has two nodes

# Create and edge between n and n1
n._add_neighbour(n1) # Take as an argument a node from the 'graph' variable
# the newly created edge is accesible by:
e = graph.E[-1]

# int that represents how many neighbours does the node have
n.num_neighbours

# dict[Node, int] Represents how many connections to a neighbouring node this node has.
n.neighbours

# list[Edge] list of edges this node is a member of.
n.edges

# id of the node.
n.id
```

#### Edge - <pl: krawędź>
```py
graph.connect_nodes(n1, n2)
new_edge = graph.E[-1]

# id of the edge. every new edge gets an incremented id.
new_edge.id

# list of nodes it connects
new_edge.nodes
```

#### SimpleEdge <pl: Zwyczajna krawędź?> 
##### Na pewno łączy dokładnie dwa wierzchołki

```py
graph = SimpleGraph()    # both graph types use this type of edges
graph = Multigraph()

# in this example I didn't create two edges
# you would have to do it manulay by connecting two nodes (that also would have to be created)

simple_edge: SimpleEdge = graph.E[-1]

# Check if two edges are equal
# returns true if edge consists of two same nodes.
are_equal: bool = simple_edge.equal_to(graph.E[-2])

# you can access nodes by:
simple_edge.nodes # the same way as with Edge object, because SimpleEdge is a child of Edge.
simple_edge.n1
simple_edge.n2
```


#### DirectedGraph - <pl: graf kierunkowy / digraf>
##### graph's edges are an instance of DirectedEdge.
```
dg = DirectedGraph()

from_node, to_node = dg.add_nodes(2)

# This method is different from previous because the order of nodes as arugments is important
dg.connect_nodes(from_node, to_node)

# It does not introduce any new methods, but it uses DirectedEdge, which has different
directed_edge: DirectedEdge = dg.E[-1]
```


#### DirectedEdge - <pl: krawęź skierowana>
##### It has a direction
```
# assuming n1 and n2 are nodes of this edge (you have to create them manulay in you code)
directed_edge.flow_possible(n1, n2) 

# check if this directed edge connects two same nodes as the other edge and if they have the same flow direction
directed_edge.equal_to(dg.E[1])     

# So how to find the direction?
# access nodes in this edge
directed_edge.from_     # this is the direction: from_ -> to
directed_edge.to
```