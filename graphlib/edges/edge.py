from __future__ import annotations
from typing import TYPE_CHECKING

from ..errors.errors import NodeNotMemberOfEdgeError

if TYPE_CHECKING:
    from ..nodes.node import Node

class Edge:
    def __init__(self, graph, *nodes: Node) -> None:
        self.graph = graph
        self.nodes: list[Node] = []
        
        self.id = None
        # when appending to a graph (USING AN APPROPRIATE METHOD - Graph.add_edges(edge)),
        # the graph will automatically set the id.
        
        for n in nodes:
            self._connect_node(n)
        
        # for visualization purposes
        self.color = None
        self.width = None
        self.to_visualize = ""

    def __str__(self) -> str:
        return "".join([f"{n.id}, " for n in self.nodes]) +  "\b\b"
        
    def _connect_node(self, n_new: Node):
        for n in self.nodes:
            n._increment_neighbour_count(n_new)
            n_new._increment_neighbour_count(n)
        self.nodes.append(n_new)
        n_new.edges.append(self)

    def _disconnect_node(self, n_old: Node):
        """
        remove first occurance of node in edge    
        """
        if n_old not in self.nodes:
            raise NodeNotMemberOfEdgeError
        self.nodes.remove(n_old)
        n_old.edges.remove(self)
        for n in self.nodes:
            n._decrement_neighbour_count(n_old)
            n_old._decrement_neighbour_count(n)

    def _disconnect_all_nodes(self):
        """
        disconnect all nodes
        """
        for n in self.nodes[:]:
            self._disconnect_node(n)
