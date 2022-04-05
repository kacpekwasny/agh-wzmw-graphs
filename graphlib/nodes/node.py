from __future__ import annotations
from copy import copy

from ..edges.edge import Edge
from ..errors.errors import NodeMissingIdNodeError

class Node:
    def __init__(self, id_=None) -> None:
        """
            params:
                parent_graph: GraphBase - graph that this node is a part of
                id_: int - To allow easier interactions for user 
        """
        if id_ is None:
            raise NodeMissingIdNodeError
        self._neighbours: dict[Node, int] = {} # Node -> times it is connected to self.
        self.edges: list[Edge] = []
        self.id = id_            

    def _add_neighbour(self, n: Node):
        """Increment neighbour dict count"""
        if n in self._neighbours:
            self._neighbours[n] += 1
            return
        self._neighbours[n] = 1

    def _remove_neighbour(self, n: Node):
        """Decrement neighbour dict count"""
        self._neighbours[n] -= 1  

    @property
    def neighbours(self) -> dict[Node, int]:
        return copy(self.neighbours)

    def _join_node_to_edge(self, e: Edge):
        e._connect_node(self)

    @property
    def num_neighbours(self) -> int:
        return len([None for v in self._neighbours.values() if v != 0])


        


    