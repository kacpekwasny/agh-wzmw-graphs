from typing import Type

from ..errors import GraphError

class Node: pass
class Node:
    def __init__(self, parent_graph) -> None:
        self.parent_graph = parent_graph
        self.neighbours = []
    
    """
    add_neighbours_ adds nodes
    """
    def add_neighbours_(self, *nodes: Type[Node]):
        for n in nodes:
            if n.parent_graph is not self.parent_graph:
        self.neighbours += nodes
    