from __future__ import annotations
from typing import Type

from ..edges.edge import Edge
from ..graphs.graph_base import GraphBase
from ..errors.errors import EdgeNotFoundNodeError, NodeMissingIdNodeError, NodeMissingIdNodeError, NodeNotFoundNodeError, NodeNotMemberOfEdgeError, WrongGraphParentNodeError

class Node:
    def __init__(self, parent_graph: GraphBase, id_=None) -> None:
        self.parent_graph: GraphBase = parent_graph
        self.neighbours: list[Node] = []
        self.edges: list[Edge] = []
        if id_ is None:
            raise NodeMissingIdNodeError
        self.id = id_
    
    """
    add_neighbours adds nodes to neighbours if this node allready is not present in neighbours
    """
    def __add_neighbours(self, *nodes: Node):
        for n in nodes:
            if n.parent_graph is not self.parent_graph:
                raise WrongGraphParentNodeError
            self.neighbours.append(n)

    """
    removes nodes from self.neighbours
        params:
            nodes: list[Node] - remove nodes
        raises:
            NodeNotFoundNodeError: NodeError - one of nodes to be removed from
    """
    def __remove_neighbour(self, *nodes: Node):
        for n in nodes:
            try:
                self.neighbours.remove(n)
            except ValueError:
                raise NodeNotFoundNodeError

    """
    append edge to edges of this node if this node is a part of this edge
        raises:
            NodeNotMemberOfEdgeError: EdgeError
    """
    def __add_edge(self, e: Edge):
        if self not in e.nodes:
            raise NodeNotMemberOfEdgeError
        self.edges.append(e)

    """
    remove edge, and remove edge.nodes from neighbours of this node !!!! but only if other edge doesnt connect this node to that other

        params:
            e: Edge
        
        raises:
            NodeNotMemberOfEdgeError:   EdgeError - this node is not member of edge.nodes
            EdgeNotFoundNodeError:      NodeError - this edge is not member of node.edges
    """
    def __remove_edge(self, e: Edge):
        if self not in e.nodes:
            raise NodeNotMemberOfEdgeError
        if e not in self.edges:
            raise EdgeNotFoundNodeError
        self.edges.remove(e)
        for n in e.nodes:
            if n is self:
                continue
            # find if there is another edge that makes self neighbours with n
            # if so then continue
            # if not then remove n from self.neighbours
            found_node_in_other_edge = False
            for e in self.edges:
                if n in e.nodes:
                    found_node_in_other_edge = True
                    break
            if not found_node_in_other_edge:
                self.
                


    """
    Join this node to edge. Append edge to this node's edges if this node is a part of this edge's nodes.
        params:
            e: Edge - to be connected to
        
        raises:
            NodeNotMemberOfEdgeError: EdgeError - trying to connect a node to an edge that it is not a member of
    """
    def join_node_to_edge(self, e: Edge):
        if self not in e.nodes:
            raise NodeNotMemberOfEdgeError
        self.__add_neighbours([n for n in e.nodes if n is not self])
        self.__add_edge(e)


    """
    Remove edge from edges, remove nodes from neighbours !but only if they
    """
    def disconnect_node_from_edge(self, e: Edge):
        if e not in self.edges:
            raise EdgeNotFoundNodeError
        


        


    