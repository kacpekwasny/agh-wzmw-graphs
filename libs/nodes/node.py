from __future__ import annotations
from itertools import count
from typing import Type

from ..edges.edge import Edge
from ..graphs.graph_base import GraphBase
from ..errors.errors import EdgeNotFoundNodeError, NodeMissingIdNodeError, NodeMissingIdNodeError, NodeNotFoundNodeError, NodeNotMemberOfEdgeError, WrongGraphParentNodeError

class Node:
    def __init__(self, id_=None) -> None:
        """
            params:
                parent_graph: GraphBase - graph that this node is a part of
                id_: int - To allow easier interactions for user 
        """
        if id_ is None:
            raise NodeMissingIdNodeError
        self.neighbours: dict[Node, int] = {} # Node -> times it is connected to self.
        self.edges: list[Edge] = []
        self.id = id_
    

    def __add_neighbours(self, *nodes: Node):
        """
        add_neighbours adds nodes to neighbours and increments the neighbours count for that node
        If an error was raised no changes were commited to the node.
            raises:
                WrongGraphParentNodeError: NodeError - if the node to become neighbour has a different graph as a parent
        """
        for n in nodes:
            if n not in self.neighbours:
                self.neighbours[n] = 1
                continue
            self.neighbours += 1    

    def __remove_neighbour(self, *nodes: Node):
        """
        removes decrements self.neighbours[node].

            params:
                nodes: tuple[Node] - remove nodes
            raises:
                NodeNotFoundNodeError: NodeError - one of nodes to be removed from
        """
        for n in nodes:
            if n in self.neighbours:
                self.neighbours[n] -= 1
            


    def __add_edge(self, e: Edge):
        """
        append edge to edges of this node if this node is a part of this edge
            raises:
                NodeNotMemberOfEdgeError: EdgeError
        """
        if self not in e.nodes:
            raise NodeNotMemberOfEdgeError
        self.edges.append(e)


    def __remove_edge(self, e: Edge):
        """
        remove edge, and decrese count on times self and nodes from edge.nodes are neighbours in self.neighbours
        decrese count self is neighbour in others

            params:
                e: Edge
            
            raises:
                NodeNotMemberOfEdgeError:   EdgeError - this node is not member of edge.nodes
                EdgeNotFoundNodeError:      NodeError - this edge is not member of node.edges
        """
        self.edges.remove(e)
        for n in e.nodes:
            # find if there is another edge that makes self neighbours with n
            # if so then continue
            # if not then remove n from self.neighbours
            self.neighbours[n] -= 1

    def join_node_to_edge(self, e: Edge):
        """
        Join this node to edge.
        Append edge to this node's edges if this node is a part of this edge's nodes.

            params:
                e: Edge - to be connected to
            
        """
        e.connect_node(self)
        return
        e.nodes.append(self)
        self.__add_neighbours(e.nodes)
        self.__add_edge(e)


    def disconnect_node_from_edge(self, e: Edge):
        """
        Remove edge from edges, decreses the count nodes are neighbours
            raises:
                EdgeNotFoundNodeError: NodeError - this edge was not found in node's edges
        """
        e.disconnect_node(self)
        return 
        if e not in self.edges:
            raise EdgeNotFoundNodeError
        self.__remove_edge(e)
        

    @property
    def num_neighbours(self) -> int:
        return len([None for v in self.neighbours.values() if v != 0])


        


    