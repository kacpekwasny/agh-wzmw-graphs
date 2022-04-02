from __future__ import annotations

from ..nodes.node import Node
from .edge import Edge

class SimpleEdge(Edge):
    def __init__(self, n1: Node, n2: Node) -> None:
        # it just might be usefull, to have aliases
        # AND cleaner
        self.n1 = n1
        self.n2 = n2
        super().__init__(n1, n2)
    
    """
    Compare two edges:

        returns:
            self and other connects two same nodes
    """
    def equal_to(self, other: SimpleEdge) -> bool:
        sn, on = self.nodes, other.nodes
        if (sn[0] == on[0] and sn[1] == on[1]
         or sn[0] == on[1] and sn[1] == on[0]):
            return True
        return False
