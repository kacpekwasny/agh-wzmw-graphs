from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..nodes.node import Node

class Edge:
    def __init__(self, *nodes: Node) -> None:
        self.nodes = nodes
        


