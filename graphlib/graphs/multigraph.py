from ..errors.errors import EdgeNotMemberOfGraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .simple_graph import SimpleGraph


class Multigraph(SimpleGraph):
    """
    Very much similar to SimpleGraph, but with the difference, that you can create many edges between two nodes.
    """
    def connect_nodes(self, n1: node.Node, n2: node.Node):
        """Create an edge between two nodes even when an exact one allready exists."""
        new_e = se.SimpleEdge(n1, n2)
        super()._add_edge(new_e)
