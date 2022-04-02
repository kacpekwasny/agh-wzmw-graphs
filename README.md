# agh-wzmw-graphs

Learn few algorithms from Graph Theory in a fun way, but I also want to make it flexible.


Hello world! Simple graph:

```py
from graphlib.graphs.simple_graph import SimpleGraph
from copy import deepcopy


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
    {n2.neighbours[n1] = }
    {n1.neighbours[n2] = }
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
```py
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
    n2.neighbours[n1] = 1
    n1.neighbours[n2] = 1
This displays what edges is this node part of.
    [str(e) for e in n1.edges] = ['0<=>1', '0<=>9']
    [str(e) for e in n2.edges] = ['0<=>1', '1<=>2']

G1.remove_edge(e)

This displays how many connections to a certain node does this node have:
    n2.neighbours[n1] = 0
    n1.neighbours[n2] = 0
This displays what edges is this node part of.
    [str(e) for e in n1.edges] = ['0<=>9']
    [str(e) for e in n2.edges] = ['1<=>2']
```