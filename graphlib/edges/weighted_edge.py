from .simple_edge import SimpleEdge
from ..nodes.node import Node

class WeightedEdge(SimpleEdge):
    def __init__(self, graph, n1: Node, n2: Node, *, weight=0, flow=1, capacity=1) -> None:
        self.weight = weight
        self.flow = flow
        self.capacity = capacity
        super().__init__(graph, n1, n2)
