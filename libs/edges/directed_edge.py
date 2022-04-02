from __future__ import annotations
from typing import TYPE_CHECKING

from .edge import Edge

if TYPE_CHECKING:
    from ..nodes.node import Node

class DirectedEdge(Edge):
    def __init__(self, from_: Node, to: Node) -> None:
        self.from_ = from_
        self.to = to
        super().__init__(from_, to)
    
    def equal_to(self, other: DirectedEdge):
        return self.from_ == other.from_ and self.to == other.to




