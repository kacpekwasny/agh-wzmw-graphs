from typing import Type, TYPE_CHECKING

from ..edges import edge
from ..nodes import node
from ..errors.errors import NodeNotFoundNodeError, NodeNotFoundNodeError
    

class GraphBase:
    def __init__(self) -> None:
        self.V: list[node.Node] = [] # vertecies / nodes
        self.E: list[edge.Edge] = [] # edges
        self.__last_inserted_node_id = 0 # increment +1 on every new Node


    """
    Create a node and append to graphs Vertices
        returns:
            (Node) the created node
    """
    def add_node(self):
        n = node.Node(id_=self.__last_inserted_node_id+1)
        self.__last_inserted_node_id += 1
        self.V.append(n)
        return n

    """
    Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
    """    
    def remove_node(self):
        raise NotImplemented

    """
    Raise a NodeNotFoundError when nodes are not members of the vertices of the graph.
        raises:
            NodeNotFoundError:  when nodes are not members of the vertices of the graph
    """
    def nodes_are_members(self, *nodes):
        for n in nodes:
            if n not in self.V:
                raise NodeNotFoundNodeError

    def add_edge(self, edge: edge.Edge):
        self.E.append(edge)
