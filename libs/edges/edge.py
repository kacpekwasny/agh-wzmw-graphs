from __future__ import annotations
from typing import TYPE_CHECKING

from ..errors.errors import NodeNotMemberOfEdgeError

if TYPE_CHECKING:
    from ..nodes.node import Node

class Edge:
    def __init__(self, *nodes: Node) -> None:
        self.nodes = list(nodes)
        
    def connect_node(self, n_new: Node):
        for n in self.nodes:
            if n_new in n.neighbours:
                n.neighbours[n] += 1
                continue
            n.neighbours[n_new] = 1
        self.nodes.append(n_new)

    def disconnect_node(self, n_old: Node):
        """
        remove first occurance of node in edge    
        """
        if n_old not in self.nodes:
            raise NodeNotMemberOfEdgeError
        self.nodes.remove(n_old)
        for n in self.nodes:
            n.neighbours[n_old] -= 1
            n_old[n] -= 1
        

