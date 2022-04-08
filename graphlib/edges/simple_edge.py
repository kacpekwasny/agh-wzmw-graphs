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
    
    def __str__(self) -> str:
        return f"{self.n1.id}<=>{self.n2.id}"

    def _disconnect_node(self, n_old: Node):
        """
        In simple edge, when you disconnect one node from edge, it means, that there is only one node left,
        so I automatically disconnect there other edge as well.
        """
        super()._disconnect_node(n_old)

    def equal_to(self, other: SimpleEdge) -> bool:
        """
        Compare two edges:

            returns:
                self and other connects two same nodes
        """
        sn, on = self.nodes, other.nodes
        if (sn[0] == on[0] and sn[1] == on[1]
         or sn[0] == on[1] and sn[1] == on[0]):
            return True
        return False
