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

    def join_node_to_edge(self, e: Edge):
        e.connect_node(self)

    def disconnect_node_from_edge(self, e: Edge):
        e.disconnect_node(self)

    @property
    def num_neighbours(self) -> int:
        return len([None for v in self.neighbours.values() if v != 0])


        


    