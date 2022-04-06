from __future__ import annotations
from typing import TYPE_CHECKING

from graphlib.errors.errors import NodeNotMemberOfEdgeError

from .edge import Edge

if TYPE_CHECKING:
    from ..nodes.node import Node

class DirectedEdge(Edge):
    def __init__(self, from_: Node, to: Node) -> None:
        self.from_ = from_
        self.to = to
        super().__init__(from_, to)
    
    def __str__(self) -> str:
        return f"{self.from_.id}=>{self.to.id}"


    def equal_to(self, other: DirectedEdge):
        return self.from_ == other.from_ and self.to == other.to

    def flow_possible(self, from_, to) -> bool:
        """
        Tell if this edge is directed in direction from_ -> to
            raises:
                EdgeError - when at least one node is not a member of this edge
            returns:
                bool - this edge allows flow from_ -> to
        """
        if not (from_ in self.nodes and to in self.nodes):
            return NodeNotMemberOfEdgeError
        return from_ == self.from_ and to == self.to



