from __future__ import annotations

from .algo import Algo

from ..errors.errors import NoNodesGraphError
from ..graphs.graph_base import GraphBase
from ..nodes.node import Node
from ..edges.edge import Edge

class IsConnected(Algo):
    """
    A path from any node of a graph can be found to any other one 
    """

    def prepare(self, graph: GraphBase):
        self.graph = graph
        self.nodes = graph.V[:]
        self.connected_nodes: list[Node] = []
        self.node_queue: list[Node] = []
        try:
            self.connected_nodes.append(self.nodes[0])
            self.node_queue.append(self.nodes[0])
        except IndexError:
            raise NoNodesGraphError

    def next(self) -> bool:
        """
        Execute a loop of the algorithm
            returns:
                bool: True if there is a next step to be executed. False if algorithm is completed.
        """
        if len(self.node_queue) == 0:
            self.done = True
            return False
        self.node = self.node_queue.pop(0)
        for e in self.node.edges:
            for n in e.nodes:
                if n in self.connected_nodes:
                    continue
                # This node has not been discovered yet
                self.connected_nodes.append(n)
                self.node_queue.append(n)
        return True

    def return_value(self) -> bool:
        return all([n in self.connected_nodes for n in self.graph.V])


    def solve(self, graph: GraphBase) -> IsConnected:
        self.prepare(graph)
        while self.next(): pass
        return self





