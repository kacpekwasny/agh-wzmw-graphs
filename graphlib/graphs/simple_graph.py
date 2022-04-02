from ..errors.errors import EdgeNotMemberOfGraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .graph_base import GraphBase


class SimpleGraph(GraphBase):
    def __init__(self) -> None:
        super().__init__()

    def add_node(self):
        """Create a node append it to self and return the instance."""
        return super()._add_node()

    def remove_node(self, n):
        """
        Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
        """
        super()._remove_node(n)

    def connect_nodes(self, n1: node.Node, n2: node.Node):
        """Create an edge between two nodes unles it allready exists."""
        new_e = se.SimpleEdge(n1, n2)
        for e in self.E:
            if new_e.equal_to(e):
                raise NodesAllreadyConnectedGraphError
        super()._add_edge(new_e)
    
    def remove_edge(self, e: se.SimpleEdge):
        """Disconnect two neighbours"""
        super()._remove_edge(e)

    def disconnect_nodes(self, n1: node.Node, n2: node.Node):
        """
        remove edge if nodes connected
            params:
                n1, n2: Node

            raises:
                GraphError
                    - At least one node is not a memeber of graph
                    - Nodes are not connected
        """
        self._nodes_are_members(n1, n2)
        e: se.SimpleEdge
        for e in n1.edges:
            if (e.n1 == n1 and e.n2 == n2
             or e.n1 == n2 or e.n2 == n1):
                self.remove_edge(e)
                return
        raise NodesNotConnectedGraphError
