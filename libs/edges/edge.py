from __future__ import annotations
from typing import TYPE_CHECKING

from ..errors.errors import NodeNotMemberOfEdgeError

if TYPE_CHECKING:
    from ..nodes.node import Node

class Edge:
    def __init__(self, *nodes: Node) -> None:
        self.nodes: list[Node] = []
        for n in nodes:
            self.connect_node(n)
        
    def connect_node(self, n_new: Node):
        for n in self.nodes:
            n.add_neighbour(n_new)
            n_new.add_neighbour(n)
        self.nodes.append(n_new)
        n_new.edges.append(self)

    def disconnect_node(self, n_old: Node):
        """
        remove first occurance of node in edge    
        """
        if n_old not in self.nodes:
            raise NodeNotMemberOfEdgeError
        self.nodes.remove(n_old)
        n_old.edges.remove(self)
        for n in self.nodes:
            n.remove_neighbour(n_old)
            n_old.remove_neighbour(n)

    def destroy(self):
        """
        disconnect all nodes
        """
        for n in self.nodes:
            self.disconnect_node(n)
