from __future__ import annotations

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
        self.neighbours: dict[Node, int] = {} # Node -> times it is connected to self.
        self.edges: list[Edge] = []
        self.id = id_            

    def add_neighbour(self, n: Node):
        if n in self.neighbours:
            self.neighbours[n] += 1
            return
        self.neighbours[n] = 1

    def remove_neighbour(self, n: Node):
        self.neighbours[n] -= 1  

    def join_node_to_edge(self, e: Edge):
        e.connect_node(self)

    def disconnect_node_from_edge(self, e: Edge):
        e.disconnect_node(self)

    @property
    def num_neighbours(self) -> int:
        return len([None for v in self.neighbours.values() if v != 0])


        


    