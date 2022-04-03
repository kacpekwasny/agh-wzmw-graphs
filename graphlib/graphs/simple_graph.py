from ..errors.errors import CannotCreateLoopGraphError, NodesAllreadyConnectedGraphError, NodesNotConnectedGraphError
from ..nodes import node
from ..edges import simple_edge as se
from .graph_base import GraphBase


class SimpleGraph(GraphBase):
    def __init__(self) -> None:
        super().__init__()

    def add_node(self):
        """Create a node append it to self and return the instance."""
        return super()._add_node()
    
    def add_nodes(self, num):
        return super()._add_nodes(num)

    def remove_node(self, n):
        """
        Remove node from Graph.V, destroy all of its edges, and remove from other nodes's neighbours.
        """
        super()._remove_node(n)

    def connect_nodes(self, n1: node.Node, n2: node.Node):
        """Create an edge between two nodes unles it allready exists."""
        if n1 is n2:
            raise CannotCreateLoopGraphError
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

    def create_path(self, *nodes: node.Node) -> None: 
        for i, n in enumerate(nodes[:-1]):
            self.connect_nodes(n, nodes[i+1])

    def create_path_ids(self, *ids: int) -> None:
        for i, id_ in enumerate(ids[:-1]):
            self.connect_nodes(self.get_nodes(id_)[0], self.get_nodes(ids[i+1])[0])
